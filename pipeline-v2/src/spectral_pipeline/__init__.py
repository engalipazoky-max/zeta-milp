"""
Unified Mathematical Pipeline for Spectral Analysis & Control.
Version 2.0 - Certified Computational Framework
"""

__version__ = "2.0.0"
__author__ = "Ali Pazoky"
__email__ = "eng.ali.pazoky@gmail.com"

from .pipeline import SpectralPipeline
from .data.zeta_zeros import LMFDBZetaZeros
from .data.synthetic import SyntheticSequence
from .math_core.statistics import (
    cosmic_harmony_statistic, 
    convergence_bound, 
    validate_convergence,
    A_CONSTANT,
    B_CONSTANT, 
    C_GUE
)
from .representation.lie_group import LieGroupSpectralCompression
from .representation.raw import RawRepresentation
from .representation.milp import MILPSubsetSelection
from .control.cal_controller import CALController
from .evaluation.metrics import evaluate_pipeline

__all__ = [
    "SpectralPipeline",
    "LMFDBZetaZeros",
    "SyntheticSequence", 
    "cosmic_harmony_statistic",
    "convergence_bound",
    "validate_convergence",
    "LieGroupSpectralCompression",
    "RawRepresentation",
    "MILPSubsetSelection",
    "CALController",
    "evaluate_pipeline",
    "A_CONSTANT",
    "B_CONSTANT",
    "C_GUE"
]