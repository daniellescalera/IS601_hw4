# pylint: disable=missing-module-docstring, missing-function-docstring
"""This module contains the main functionality for the calculator application."""
from decimal import Decimal
import pytest
from faker import Faker
from calculator.operations import Operations  # import correct class
#also having to make sure that all of the imports are in the correct order


fake = Faker()

def test_addition():
    """Testing the addition function"""
    assert Operations.add(Decimal(2), Decimal(2)) == Decimal(4)
    assert Operations.add(Decimal(-1), Decimal(1)) == Decimal(0)
    assert Operations.add(Decimal(0.5), Decimal(0.5)) == Decimal(1.0)

def test_subtraction():
    """Testing the subtraction function"""
    assert Operations.subtract(Decimal(2), Decimal(2)) == Decimal(0)
    assert Operations.subtract(Decimal(-5), Decimal(-5)) == Decimal(0)
    assert Operations.subtract(Decimal(10), Decimal(5)) == Decimal(5)

def test_multiplication():
    """Testing the multiplication function"""
    assert Operations.multiply(Decimal(3), Decimal(7)) == Decimal(21)
    assert Operations.multiply(Decimal(-5), Decimal(5)) == Decimal(-25)
    assert Operations.multiply(Decimal(0), Decimal(4)) == Decimal(0)

def test_division():
    """Testing the division function"""
    assert Operations.divide(Decimal(6), Decimal(3)) == Decimal(2)
    assert Operations.divide(Decimal(5), Decimal(2)) == Decimal("2.5")
    assert Operations.divide(Decimal(-6), Decimal(3)) == Decimal(-2)

def test_division_by_zero():
    """Testing division by zero exception"""
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        Operations.divide(Decimal(5), Decimal(0))

# ------------------- Faker-Based Randomized Tests ------------------- #

def test_random_addition():
    """Testing addition using Faker-generated random numbers"""
    a = Decimal(fake.random_int(min=-100, max=100))
    b = Decimal(fake.random_int(min=-100, max=100))
    expected = a + b
    assert Operations.add(a, b) == expected

def test_random_subtraction():
    """Testing subtraction using Faker-generated random numbers"""
    a = Decimal(fake.random_int(min=-100, max=100))
    b = Decimal(fake.random_int(min=-100, max=100))
    expected = a - b
    assert Operations.subtract(a, b) == expected

def test_random_multiplication():
    """Testing multiplication using Faker-generated random numbers"""
    a = Decimal(fake.random_int(min=-50, max=50))
    b = Decimal(fake.random_int(min=-50, max=50))
    expected = a * b
    assert Operations.multiply(a, b) == expected

def test_random_division():
    """Testing division using Faker-generated random numbers"""
    a = Decimal(fake.random_int(min=1, max=100))
    b = Decimal(fake.random_int(min=1, max=100))  # Avoid zero for divide-by-zero error
    expected = a / b
    assert Operations.divide(a, b) == expected
