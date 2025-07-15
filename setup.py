#!/usr/bin/env python3
"""
Memory Quantum System - Setup Script
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="memory-quantum-system",
    version="1.0.0",
    author="Memory Quantum System Development Team",
    author_email="info@memory-quantum.com",
    description="使うほど賢くなる学習型記憶データベース",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/memory-quantum/memory-quantum-system",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Database",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=[
        # 標準ライブラリのみ使用
    ],
    extras_require={
        "dev": [
            "pytest",
            "pytest-cov",
            "black",
            "flake8",
            "mypy",
        ],
    },
    entry_points={
        "console_scripts": [
            "memory-quantum=memory_quantum_system:main",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/memory-quantum/memory-quantum-system/issues",
        "Documentation": "https://memory-quantum.github.io/docs/",
        "Source": "https://github.com/memory-quantum/memory-quantum-system/",
    },
)