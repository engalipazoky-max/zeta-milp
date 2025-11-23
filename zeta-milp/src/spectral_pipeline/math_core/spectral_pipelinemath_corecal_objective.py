"""CAL (Convergence-Aware Learning) objective functional."""
import numpy as np
from typing import Callable

def cal_objective(
    potential_grad_norm: float,
    spectral_deviation: float,
    mu: float = 1.0
) -> float:
    """Compute CAL objective functional: ℒ = ‖∇V‖² + μ|S_N - C_⋆|².
    
    Args:
        potential_grad_norm: Squared norm of potential gradient
        spectral_deviation: Deviation |S_N - C_⋆|
        mu: Regularization parameter
        
    Returns:
        CAL objective value
    """
    return potential_grad_norm + mu * (spectral_deviation ** 2)

def cal_gradient(
    alpha: np.ndarray,
    potential_grad_fn: Callable[[np.ndarray], np.ndarray],
    spectral_grad_fn: Callable[[np.ndarray], float],
    S_N: float,
    mu: float = 1.0
) -> np.ndarray:
    """Compute gradient of CAL objective w.r.t. parameters α.
    
    Args:
        alpha: Parameter vector
        potential_grad_fn: Function computing ∇_α ‖∇V‖²
        spectral_grad_fn: Function computing ∇_α |S_N - C_⋆|²  
        S_N: Current spectral statistic
        mu: Regularization parameter
        
    Returns:
        Gradient ∇_α ℒ
    """
    grad_potential = potential_grad_fn(alpha)
    grad_spectral = spectral_grad_fn(alpha)
    
    return grad_potential + mu * 2 * (S_N - C_GUE) * grad_spectral