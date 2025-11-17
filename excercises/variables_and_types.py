#!/usr/bin/env python3
"""
variables_and_types.py
Part of practice-python-for-beginners / python-basics-and-syntax
Licensed under GNU GPLv3
https://www.gnu.org/licenses/gpl-3.0.html

This script introduces variables and data types in Python.
"""

# Integer, float, string, and boolean examples
integer_example = 42         # Integer
float_example = 3.14159      # Float
string_example = "Hello, Python!"  # String
boolean_example = True       # Boolean

def describe_variable(var):
    """
    Returns a string describing the type and value of a variable.

    Args:
        var (any): The variable to describe.

    Returns:
        str: Description of type and value.
    """
    return f"The value '{var}' is of type {type(var).__name__}."

if __name__ == "__main__":
    # Demonstrate the types
    print(describe_variable(integer_example))
    print(describe_variable(float_example))
    print(describe_variable(string_example))
    print(describe_variable(boolean_example))
