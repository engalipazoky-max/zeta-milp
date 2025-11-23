"""Test installation and basic functionality."""
import pytest
import sys

def test_python_version():
    """Test Python version compatibility."""
    assert sys.version_info >= (3, 9)

def test_import():
    """Test that package can be imported."""
    import spectral_pipeline
    assert spectral_pipeline.__version__ is not None

def test_core_modules():
    """Test that core modules can be imported."""
    from spectral_pipeline.data import DataSource, LMFDBZetaZeros
    from spectral_pipeline.math_core import statistics
    from spectral_pipeline.representation import lie_group
    from spectral_pipeline.control import cal_controller
    
    assert True  # All imports succeeded

def test_synthetic_data():
    """Test synthetic data generation."""
    from spectral_pipeline.data.synthetic import SyntheticSequence
    
    data_source = SyntheticSequence(n_points=100)
    sequence = data_source.load()
    
    assert len(sequence) == 100
    assert sequence[0] >= 1000