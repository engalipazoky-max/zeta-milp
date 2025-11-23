"""Base representation layer interface."""
from abc import ABC, abstractmethod
import numpy as np

class Representation(ABC):
    """Abstract base class for sequence representations."""
    
    @abstractmethod
    def transform(self, sequence: np.ndarray) -> np.ndarray:
        """Transform sequence to alternative representation."""
        pass
    
    @abstractmethod
    def inverse_transform(self, transformed: np.ndarray) -> np.ndarray:
        """Reconstruct sequence from representation."""
        pass