import pytest
from exercises.basic_operations import add_numbers, divide_numbers

def test_add_numbers():
    assert add_numbers(3, 5) == 8

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide_numbers(5, 0)
