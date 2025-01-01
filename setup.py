from setuptools import setup, find_packages

setup(
    name="windows-qpu-middleware",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'cirq>=1.0.0',
        'numpy>=1.21.0',
        'pywin32>=305',
        'logging-handler>=1.0.0',
        'typing-extensions>=4.0.0',
    ],
    author="Quantum Team",
    description="Windows QPU Middleware for Quantum-Classical Integration",
    python_requires='>=3.8',
)
