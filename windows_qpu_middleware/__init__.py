"""
Windows QPU Middleware
=====================

A middleware package for integrating quantum processing units (QPUs) with Windows systems.
Provides simulation capabilities and interfaces for quantum-classical hybrid computing.
"""

from .qpu_interface import QPUInterface
from .circuit_manager import CircuitManager
from .windows_service import WindowsQPUService

__version__ = "0.1.0"
__all__ = ['QPUInterface', 'CircuitManager', 'WindowsQPUService']
