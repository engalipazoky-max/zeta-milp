"""Evaluation metrics for pipeline performance."""
import numpy as np
from typing import Dict
from ..math_core.statistics import C_GUE, cosmic_harmony_statistic

def compute_deviation(normalized_gaps: np.ndarray) -> float:
    """Compute |S_N - C_GUE| deviation metric."""
    S_N = cosmic_harmony_statistic(normalized_gaps)
    return abs(S_N - C_GUE)

def compute_reconstruction_error(original: np.ndarray, reconstructed: np.ndarray) -> float:
    """Compute normalized reconstruction error."""
    return np.linalg.norm(original - reconstructed) / np.linalg.norm(original)

def compute_parameter_stability(alpha_sequence: np.ndarray) -> Dict[str, float]:
    """Compute stability metrics for parameter evolution."""
    if len(alpha_sequence) < 2:
        return {"mean_change": 0.0, "max_change": 0.0}
    
    changes = np.diff(alpha_sequence, axis=0)
    norms = np.linalg.norm(changes, axis=1)
    
    return {
        "mean_change": float(np.mean(norms)),
        "max_change": float(np.max(norms)),
        "final_change": float(norms[-1] if len(norms) > 0 else 0.0)
    }

def evaluate_pipeline(
    original_sequence: np.ndarray,
    processed_sequence: np.ndarray,
    alpha_history: np.ndarray
) -> Dict[str, float]:
    """Comprehensive pipeline evaluation."""
    deviation = compute_deviation(processed_sequence)
    reconstruction_error = compute_reconstruction_error(original_sequence, processed_sequence)
    stability = compute_parameter_stability(alpha_history)
    
    return {
        "deviation_from_GUE": deviation,
        "reconstruction_error": reconstruction_error,
        **stability
    }