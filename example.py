"""
Example usage of Windows QPU Middleware
"""

from windows_qpu_middleware import QPUInterface, CircuitManager
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    """
    Demonstrate middleware functionality with a simple example
    """
    logger.info("Starting Windows QPU Middleware Example")
    
    # Initialize QPU interface and circuit manager
    qpu = QPUInterface()
    circuit_manager = CircuitManager(qpu)
    
    # Example 1: Pattern Recognition
    logger.info("\n=== Pattern Recognition Example ===")
    pattern_data = [0.5, 0.3, 0.8, 0.1]
    logger.info(f"Input pattern: {pattern_data}")
    
    pattern_result = circuit_manager.run_pattern_recognition(pattern_data)
    logger.info(f"Pattern detected: {pattern_result['pattern_detected']}")
    logger.info(f"Confidence score: {pattern_result['confidence']:.3f}")
    
    # Example 2: Optimization
    logger.info("\n=== Optimization Example ===")
    optimization_params = [0.1, 0.4, 0.6, 0.8]
    logger.info(f"Optimization parameters: {optimization_params}")
    
    opt_result = circuit_manager.run_optimization(optimization_params)
    logger.info(f"Optimal solution: {opt_result['optimal_solution']}")

if __name__ == "__main__":
    main()
