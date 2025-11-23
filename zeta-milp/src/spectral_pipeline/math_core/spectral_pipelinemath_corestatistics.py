"""Mathematical core: Spectral statistics and convergence analysis."""
import numpy as np
from typing import Tuple

# Empirical constants from rigorous analysis
A_CONSTANT = 2.5
B_CONSTANT = 3.0
C_GUE = 0.60338  # GUE adjacent spacing product constant

def cosmic_harmony_statistic(normalized_gaps: np.ndarray) -> float:
    """Compute S_N = (N-2)⁻¹ ∑ γ̃_k γ̃_{k+1}.
    
    Args:
        normalized_gaps: Array of normalized gaps γ̃_k
        
    Returns:
        S_N statistic measuring sequential correlation
    """
    if len(normalized_gaps) < 3:
        raise ValueError("Need at least 3 gaps for S_N computation")
    
    products = normalized_gaps[:-1] * normalized_gaps[1:]
    return np.mean(products)

def convergence_bound(N: int, A: float = A_CONSTANT, B: float = B_CONSTANT) -> float:
    """Compute theoretical convergence bound |S_N - C_GUE| ≤ A/√N + B log N / N.
    
    Args:
        N: Sample size
        A: Convergence constant
        B: Finite-size correction constant
        
    Returns:
        Upper bound on deviation from GUE prediction
    """
    if N < 3:
        return float('inf')
    
    return A / np.sqrt(N) + B * np.log(N) / N

def validate_convergence(normalized_gaps: np.ndarray) -> dict:
    """Validate convergence bound against empirical data."""
    S_N = cosmic_harmony_statistic(normalized_gaps)
    N = len(normalized_gaps)
    bound = convergence_bound(N)
    deviation = abs(S_N - C_GUE)
    
    return {
        "S_N": S_N,
        "deviation": deviation,
        "bound": bound,
        "bound_satisfied": deviation <= bound,
        "safety_margin": bound - deviation if deviation <= bound else None
    }