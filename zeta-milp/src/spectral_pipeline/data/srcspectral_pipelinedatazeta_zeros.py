"""LMFDB zeta zeros data source implementation."""
import requests
import numpy as np
from .base import DataSource

class LMFDBZetaZeros(DataSource):
    """DataSource implementation for Riemann zeta zeros from LMFDB."""
    
    def __init__(self, height: float = 1e12, count: int = 1000):
        self.height = height
        self.count = count
        self.api_url = "https://www.lmfdb.org/api/zeros/zeta/"
    
    def load(self) -> np.ndarray:
        """Load zeta zeros from LMFDB API."""
        params = {
            "height": f"[{self.height}, {self.height + 1000}]",
            "limit": self.count,
            "format": "json"
        }
        
        response = requests.get(self.api_url, params=params, timeout=60)
        response.raise_for_status()
        
        data = response.json()
        zeros = sorted([item[0] for item in data["data"]])[:self.count]
        
        return np.array(zeros)