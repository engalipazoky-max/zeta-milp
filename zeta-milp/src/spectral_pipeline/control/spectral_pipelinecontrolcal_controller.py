"""CAL (Convergence-Aware Learning) Controller."""
import numpy as np
from typing import Callable, Optional
from ..math_core.cal_objective import cal_gradient

class CALController:
    """Gradient-based controller for spectral optimization."""
    
    def __init__(
        self,
        learning_rate: float = 0.01,
        momentum: float = 0.9,
        projection_fn: Optional[Callable] = None
    ):
        self.learning_rate = learning_rate
        self.momentum = momentum
        self.projection_fn = projection_fn
        self.velocity = None
    
    def initialize(self, alpha_shape):
        """Initialize controller state."""
        self.velocity = np.zeros(alpha_shape)
    
    def compute_update(
        self,
        alpha: np.ndarray,
        gradient: np.ndarray
    ) -> np.ndarray:
        """Compute parameter update: α_{t+1} = α_t - ηg + momentum."""
        if self.velocity is None:
            self.initialize(alpha.shape)
        
        # Momentum update
        self.velocity = self.momentum * self.velocity + self.learning_rate * gradient
        
        # Parameter update
        alpha_new = alpha - self.velocity
        
        # Project to feasible set if provided
        if self.projection_fn is not None:
            alpha_new = self.projection_fn(alpha_new)
        
        return alpha_new
    
    def compute_gradient(
        self,
        alpha: np.ndarray,
        potential_grad_fn: Callable,
        spectral_grad_fn: Callable,
        S_N: float,
        mu: float = 1.0
    ) -> np.ndarray:
        """Compute CAL gradient using mathematical core."""
        return cal_gradient(alpha, potential_grad_fn, spectral_grad_fn, S_N, mu)