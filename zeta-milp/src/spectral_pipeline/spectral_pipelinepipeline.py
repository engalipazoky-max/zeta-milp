"""Unified mathematical pipeline for spectral analysis and control."""
import numpy as np
from typing import Dict, List, Optional
from .data.base import DataSource
from .representation.base import Representation
from .representation.raw import RawRepresentation
from .control.cal_controller import CALController
from .evaluation.metrics import evaluate_pipeline

class SpectralPipeline:
    """Unified pipeline for mathematical spectral analysis."""
    
    def __init__(
        self,
        data_source: DataSource,
        representation: Optional[Representation] = None,
        controller: Optional[CALController] = None
    ):
        self.data_source = data_source
        self.representation = representation or RawRepresentation()
        self.controller = controller or CALController()
        
        # Pipeline state
        self.original_sequence = None
        self.processed_sequence = None
        self.alpha_history = []
    
    def run(
        self,
        n_iterations: int = 100,
        potential_grad_fn: Optional[callable] = None,
        spectral_grad_fn: Optional[callable] = None
    ) -> Dict[str, List[float]]:
        """Execute complete pipeline.
        
        Args:
            n_iterations: Number of control iterations
            potential_grad_fn: Gradient function for potential term
            spectral_grad_fn: Gradient function for spectral term
            
        Returns:
            Dictionary of evaluation metrics over iterations
        """
        # Load and preprocess data
        self.original_sequence = self.data_source.load()
        normalized_gaps = self.data_source.normalize_gaps(self.original_sequence)
        
        # Initialize representation and controller
        transformed = self.representation.transform(normalized_gaps)
        self.processed_sequence = self.representation.inverse_transform(transformed)
        
        # Initialize parameters (example: simple scaling parameter)
        alpha = np.array([1.0])  # Initial parameter
        self.controller.initialize(alpha.shape)
        
        # Track metrics
        metrics_history = {
            "deviation": [],
            "reconstruction_error": [],
            "parameter_change": []
        }
        
        # Control loop
        for iteration in range(n_iterations):
            # Compute current metrics
            current_metrics = evaluate_pipeline(
                normalized_gaps, 
                self.processed_sequence, 
                np.array(self.alpha_history)
            )
            
            # Store metrics
            for key, value in current_metrics.items():
                if key in metrics_history:
                    metrics_history[key].append(value)
            
            # Compute gradient and update parameters
            if potential_grad_fn and spectral_grad_fn:
                from .math_core.statistics import cosmic_harmony_statistic
                S_N = cosmic_harmony_statistic(self.processed_sequence)
                
                gradient = self.controller.compute_gradient(
                    alpha, potential_grad_fn, spectral_grad_fn, S_N
                )
                
                alpha = self.controller.compute_update(alpha, gradient)
                self.alpha_history.append(alpha.copy())
            
            # Update representation with new parameters
            # (This would depend on specific parameterization)
        
        return metrics_history
    
    def get_final_metrics(self) -> Dict[str, float]:
        """Get final evaluation metrics."""
        if self.original_sequence is None or self.processed_sequence is None:
            raise ValueError("Pipeline must be run first")
        
        normalized_gaps = self.data_source.normalize_gaps(self.original_sequence)
        return evaluate_pipeline(
            normalized_gaps,
            self.processed_sequence,
            np.array(self.alpha_history)
        )