"""
Example usage of QPU Windows Middleware
"""
from windows_qpu_middleware.circuit_manager import CircuitManager
from windows_qpu_middleware.qpu_interface import QPUInterface

def main():
    # Initialize the interface
    qpu = QPUInterface()
    circuit_manager = CircuitManager(qpu)
    
    # Example 1: Pattern Recognition
    input_data = [0.5, 0.3, 0.8, 0.1]  # Your quantum data pattern
    pattern_result = circuit_manager.run_pattern_recognition(input_data)
    print("Pattern Recognition Result:", pattern_result)
    
    # Example 2: Quantum Optimization
    parameters = [0.1, 0.4, 0.6, 0.8]  # Optimization parameters
    optimization_result = circuit_manager.run_optimization(parameters)
    print("Optimization Result:", optimization_result)

if __name__ == "__main__":
    main()
