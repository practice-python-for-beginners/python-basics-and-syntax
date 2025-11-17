#!/usr/bin/env python3
"""
strings_and_formatting.py
GNU GPLv3 License
Covers basic string manipulation and formatting techniques.
"""

def greet_user(name):
    """Return a greeting message."""
    return f"Hello, {name}! Welcome to Python."

def uppercase(text):
    """Return the uppercase version of text."""
    return text.upper()

def count_characters(text):
    """Return the number of characters in text."""
    return len(text)

if __name__ == "__main__":
    name = "Alice"
    print(greet_user(name))
    print("Uppercase:", uppercase("python is fun"))
    print("Character count:", count_characters("Python!"))
  
