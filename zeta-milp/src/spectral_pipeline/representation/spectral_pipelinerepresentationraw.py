"""Raw domain representation (identity transformation)."""
import numpy as np
from .base import Representation

class RawRepresentation(Representation):
    """Identity representation: γ̃ → Controller."""
    
    def transform(self, sequence: np.ndarray) -> np.ndarray:
        return sequence.copy()
    
    def inverse_transform(self, transformed: np.ndarray) -> np.ndarray:
        return transformed.copy()