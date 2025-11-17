#!/usr/bin/env python3
"""
basic_operations.py
GNU GPLv3 License
Demonstrates basic arithmetic operations in Python.
"""

def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract_numbers(a, b):
    """Return the difference between two numbers."""
    return a - b

def multiply_numbers(a, b):
    """Return the product of two numbers."""
    return a * b

def divide_numbers(a, b):
    """
    Return the division result of two numbers.
    Prevents division by zero errors.

    Raises:
        ValueError: If b == 0
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

if __name__ == "__main__":
    print("Addition:", add_numbers(10, 5))
    print("Subtraction:", subtract_numbers(10, 5))
    print("Multiplication:", multiply_numbers(10, 5))
    print("Division:", divide_numbers(10, 5))
  
