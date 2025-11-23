"""Lie-group spectral compression using orthogonal bases."""
import numpy as np
from scipy.fft import fft, ifft
import pywt
from .base import Representation

class LieGroupSpectralCompression(Representation):
    """Spectral compression using orthogonal basis transformations."""
    
    def __init__(self, basis_type: str = 'dft', sparsity_param: float = 0.1):
        self.basis_type = basis_type
        self.sparsity_param = sparsity_param
    
    def transform(self, sequence: np.ndarray) -> np.ndarray:
        """Log map: Transform to spectral domain."""
        if self.basis_type == 'dft':
            # DFT basis transform
            return fft(sequence)
        elif self.basis_type == 'wavelet':
            # Wavelet transform (Daubechies 4)
            coeffs = pywt.wavedec(sequence, 'db4', level=4)
            return np.concatenate(coeffs)
        else:
            raise ValueError(f"Unknown basis type: {self.basis_type}")
    
    def sparse_optimization(self, coefficients: np.ndarray) -> np.ndarray:
        """Sparse optimization in spectral domain: min ‖v - w‖₂² + λ‖w‖₁."""
        # Soft thresholding for L1 regularization
        threshold = self.sparsity_param * np.max(np.abs(coefficients))
        
        if np.iscomplexobj(coefficients):
            # Complex soft thresholding
            magnitude = np.abs(coefficients)
            phase = np.exp(1j * np.angle(coefficients))
            thresholded_magnitude = np.maximum(magnitude - threshold, 0)
            return thresholded_magnitude * phase
        else:
            # Real soft thresholding
            return np.sign(coefficients) * np.maximum(np.abs(coefficients) - threshold, 0)
    
    def inverse_transform(self, transformed: np.ndarray) -> np.ndarray:
        """Exp map: Reconstruct from spectral domain."""
        if self.basis_type == 'dft':
            reconstruction = ifft(transformed).real
        elif self.basis_type == 'wavelet':
            # Determine wavelet coefficients structure
            level = 4
            coeff_slices = pywt.wavedec(np.zeros_like(transformed), 'db4', level=level)
            coeffs = []
            start = 0
            for slice_len in [len(c) for c in coeff_slices]:
                coeffs.append(transformed[start:start + slice_len])
                start += slice_len
            reconstruction = pywt.waverec(coeffs, 'db4')
        else:
            raise ValueError(f"Unknown basis type: {self.basis_type}")
        
        # Ensure real-valued output with original length
        return np.real(reconstruction)[:len(transformed)]