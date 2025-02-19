# pylint: disable=missing-module-docstring, missing-function-docstring
"""Unit tests for the calculations."""
# tests/test_calculations.py
import pytest
from calculator.calculations import Calculation
from calculator.operations import Operations

def test_operations():
    #Test basic operations.
    assert Operations.add(2, 3) == 5
    assert Operations.subtract(5, 3) == 2
    assert Operations.multiply(3, 3) == 9
    assert Operations.divide(10, 2) == 5

def test_zero_division():
    #Test division by zero exception.
    with pytest.raises(ZeroDivisionError):
        Operations.divide(5, 0)

def test_calculation():
    # Test calculation wrapper.
    calc = Calculation(2, 3, "add", 5)
    assert calc.a == 2
    assert calc.b == 3
    assert calc.operation == "add"
    assert calc.result == 5
