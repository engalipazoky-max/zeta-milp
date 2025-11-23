"""Synthetic data sources for testing and validation."""
import numpy as np
from .base import DataSource

class SyntheticSequence(DataSource):
    """Generate synthetic sequences with controlled spectral properties."""
    
    def __init__(self, n_points: int = 1000, sequence_type: str = "gue_like"):
        self.n_points = n_points
        self.sequence_type = sequence_type
    
    def load(self) -> np.ndarray:
        """Generate synthetic sequence."""
        if self.sequence_type == "gue_like":
            return self._generate_gue_like()
        elif self.sequence_type == "poisson":
            return self._generate_poisson()
        elif self.sequence_type == "deterministic":
            return self._generate_deterministic()
        else:
            raise ValueError(f"Unknown sequence type: {self.sequence_type}")
    
    def _generate_gue_like(self) -> np.ndarray:
        """Generate GUE-like spectrum using gamma distribution."""
        # Gamma distribution approximates GUE gap statistics
        gaps = np.random.gamma(shape=1.0, scale=1.0, size=self.n_points)
        return np.cumsum(gaps) + 1000  # Start at reasonable height
    
    def _generate_poisson(self) -> np.ndarray:
        """Generate Poisson-like spectrum (exponential gaps)."""
        gaps = np.random.exponential(scale=1.0, size=self.n_points)
        return np.cumsum(gaps) + 1000
    
    def _generate_deterministic(self) -> np.ndarray:
        """Generate deterministic sequence with linear spacing."""
        return np.linspace(1000, 1000 + self.n_points, self.n_points)