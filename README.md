# Windows QPU Middleware

A Windows-compatible middleware solution for integrating quantum processing units (QPUs) with classical systems. This middleware provides simulation capabilities and interfaces for quantum-classical hybrid computing.

## Features

- **Windows Service Integration**: Runs as a native Windows service
- **Quantum Circuit Management**: Create and execute quantum circuits
- **Pattern Recognition**: Quantum-enhanced pattern recognition capabilities
- **Optimization**: Quantum optimization algorithms
- **Error Mitigation**: Built-in error correction and mitigation
- **Simulation Mode**: Test quantum algorithms using Cirq simulator
- **Logging System**: Comprehensive logging and monitoring

## Installation

1. Install required dependencies:
```bash
pip install -r requirements.txt
```

2. Install the Windows service (requires Administrator privileges):
```bash
# Run Command Prompt or PowerShell as Administrator
python -m windows_qpu_middleware.windows_service install
```

## Project Structure

```
windows_qpu_middleware/
├── __init__.py              # Package initialization
├── qpu_interface.py         # Core QPU interface
├── circuit_manager.py       # Quantum circuit management
├── windows_service.py       # Windows service implementation
└── test_middleware.py       # Test suite
```

## Usage

### Basic Usage Example

```python
from windows_qpu_middleware import QPUInterface, CircuitManager

# Initialize QPU interface
qpu = QPUInterface()

# Create circuit manager
circuit_manager = CircuitManager(qpu)

# Run pattern recognition
input_data = [0.5, 0.3, 0.8, 0.1]
result = circuit_manager.run_pattern_recognition(input_data)
print(f"Pattern detected: {result['pattern_detected']}")
print(f"Confidence: {result['confidence']}")
```

### Running Tests

```bash
python -m windows_qpu_middleware.test_middleware
```

## Service Management (Requires Administrator Privileges)

### Install Service
```bash
# Run as Administrator
python -m windows_qpu_middleware.windows_service install
```

### Start Service
```bash
# Run as Administrator
python -m windows_qpu_middleware.windows_service start
```

### Stop Service
```bash
# Run as Administrator
python -m windows_qpu_middleware.windows_service stop
```

### Remove Service
```bash
# Run as Administrator
python -m windows_qpu_middleware.windows_service remove
```

## Components

### QPU Interface
- Manages quantum operations
- Handles hardware/simulation switching
- Provides error mitigation

### Circuit Manager
- Creates quantum circuits
- Manages circuit execution
- Processes results

### Windows Service
- Runs middleware as Windows service
- Handles system integration
- Manages resource allocation

## Test Results

The middleware has been tested with the following results:

### Pattern Recognition
- Successfully processes different input patterns
- Provides confidence scores for pattern detection
- Demonstrates proper circuit creation and execution

### Quantum Optimization
- Successfully optimizes various parameter sets
- Shows consistent optimal solution finding
- Proper circuit execution and result processing

### Error Mitigation
- Tested with both low (0.001) and high (0.1) error rates
- Demonstrates proper error correction
- Shows consistent results across different error levels

## Error Handling

The middleware includes comprehensive error handling:
- Hardware status monitoring
- Automatic error mitigation
- Detailed logging
- Graceful failure recovery

## Logging

Logs are stored in:
- Service logs: `C:/ProgramData/WindowsQPUMiddleware/logs/qpu_service.log`
- Middleware logs: `qpu_middleware.log`

## Requirements

- Python 3.8 or higher
- Windows 10/11
- Administrator privileges (for service installation)
- Required Python packages:
  - pywin32
  - cirq
  - numpy
  - logging-handler

## Development

### Running Tests
```bash
python -m windows_qpu_middleware.test_middleware
```

### Debug Mode
Set logging level to DEBUG for more detailed output:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Known Issues

1. Service installation requires Administrator privileges
2. Service must be installed from an elevated Command Prompt or PowerShell

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Support

For support and questions, please open an issue in the repository.
