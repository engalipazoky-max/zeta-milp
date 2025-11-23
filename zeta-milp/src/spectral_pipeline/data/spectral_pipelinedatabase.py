"""Abstract data source interface for mathematical sequences."""
from abc import ABC, abstractmethod
from typing import Optional
import numpy as np

class DataSource(ABC):
    """Abstract base class for mathematical sequence data sources."""
    
    @abstractmethod
    def load(self) -> np.ndarray:
        """Load mathematical sequence data.
        
        Returns:
            1D array representing the primary mathematical sequence
        """
        pass
    
    def normalize_gaps(self, sequence: np.ndarray) -> np.ndarray:
        """Normalize sequence gaps to unit mean spacing."""
        gaps = np.diff(sequence)
        return gaps / np.mean(gaps)

class BootstrapResampler:
    """Bootstrap resampling for mathematical sequences."""
    
    def __init__(self, block_size: Optional[int] = None):
        self.block_size = block_size
    
    def resample(self, sequence: np.ndarray, n_samples: int) -> np.ndarray:
        """Generate bootstrap samples preserving correlation structure."""
        n = len(sequence)
        block_size = self.block_size or int(np.sqrt(n))
        
        samples = []
        for _ in range(n_samples):
            # Block bootstrap sampling
            n_blocks = int(np.ceil(n / block_size))
            block_indices = np.random.randint(0, n - block_size + 1, n_blocks)
            
            bootstrap_sample = []
            for idx in block_indices:
                block = sequence[idx:idx + block_size]
                bootstrap_sample.extend(block)
            
            samples.append(np.array(bootstrap_sample[:n]))
        
        return np.array(samples)