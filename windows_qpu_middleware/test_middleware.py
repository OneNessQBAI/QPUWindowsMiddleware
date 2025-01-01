"""
Test Module for Windows QPU Middleware
====================================

Provides test cases and examples for using the QPU middleware.
"""

import logging
import numpy as np
from typing import Dict, List
from .qpu_interface import QPUInterface, QPUConfig
from .circuit_manager import CircuitManager

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def test_pattern_recognition():
    """Test the pattern recognition capabilities"""
    try:
        logger.info("\n=== Testing Pattern Recognition ===")
        
        # Initialize components
        qpu = QPUInterface(QPUConfig(num_qubits=4, simulation_mode=True))
        circuit_manager = CircuitManager(qpu)
        
        # Test data
        test_patterns = [
            [0.5, 0.3, 0.8, 0.1],  # Pattern 1
            [0.1, 0.9, 0.2, 0.7],  # Pattern 2
        ]
        
        # Run pattern recognition for each test pattern
        for i, pattern in enumerate(test_patterns):
            logger.info(f"\nProcessing Pattern {i + 1}: {pattern}")
            
            result = circuit_manager.run_pattern_recognition(
                input_data=pattern,
                shots=1000
            )
            
            logger.info(f"Pattern Detected: {result['pattern_detected']}")
            logger.info(f"Confidence Score: {result['confidence']:.3f}")
            
        return True
        
    except Exception as e:
        logger.error(f"Pattern recognition test failed: {str(e)}")
        return False

def test_optimization():
    """Test the quantum optimization capabilities"""
    try:
        logger.info("\n=== Testing Quantum Optimization ===")
        
        # Initialize components
        qpu = QPUInterface(QPUConfig(num_qubits=4, simulation_mode=True))
        circuit_manager = CircuitManager(qpu)
        
        # Test optimization parameters
        test_parameters = [
            [0.1, 0.4, 0.6, 0.8],  # Test case 1
            [0.7, 0.2, 0.5, 0.3],  # Test case 2
        ]
        
        # Run optimization for each test case
        for i, params in enumerate(test_parameters):
            logger.info(f"\nOptimization Test {i + 1}")
            logger.info(f"Parameters: {params}")
            
            result = circuit_manager.run_optimization(
                parameters=params,
                shots=1000
            )
            
            logger.info(f"Optimal Solution: {result['optimal_solution']}")
            
        return True
        
    except Exception as e:
        logger.error(f"Optimization test failed: {str(e)}")
        return False

def test_error_mitigation():
    """Test the error mitigation capabilities"""
    try:
        logger.info("\n=== Testing Error Mitigation ===")
        
        # Initialize with different error rates
        configs = [
            QPUConfig(num_qubits=2, error_rate=0.001),  # Low error
            QPUConfig(num_qubits=2, error_rate=0.1),    # High error
        ]
        
        test_data = [0.5, 0.3]
        
        for i, config in enumerate(configs):
            logger.info(f"\nTest {i + 1}: Error Rate = {config.error_rate}")
            
            qpu = QPUInterface(config)
            circuit_manager = CircuitManager(qpu)
            
            # Create and execute test circuit
            circuit = circuit_manager.create_pattern_recognition_circuit(test_data)
            results = circuit_manager.execute_with_error_mitigation(circuit)
            
            logger.info("Raw Results:")
            logger.info(results['raw_results']['counts'])
            logger.info("Mitigated Results:")
            logger.info(results['mitigated_results']['counts'])
            
        return True
        
    except Exception as e:
        logger.error(f"Error mitigation test failed: {str(e)}")
        return False

def run_all_tests():
    """Run all middleware tests"""
    logger.info("Starting Windows QPU Middleware Tests")
    
    tests = [
        ("Pattern Recognition", test_pattern_recognition),
        ("Quantum Optimization", test_optimization),
        ("Error Mitigation", test_error_mitigation),
    ]
    
    results = {}
    
    for test_name, test_func in tests:
        logger.info(f"\nRunning {test_name} Test...")
        try:
            success = test_func()
            results[test_name] = "PASSED" if success else "FAILED"
        except Exception as e:
            logger.error(f"Test error: {str(e)}")
            results[test_name] = "ERROR"
    
    # Print summary
    logger.info("\n=== Test Summary ===")
    for test_name, result in results.items():
        logger.info(f"{test_name}: {result}")

if __name__ == "__main__":
    run_all_tests()
