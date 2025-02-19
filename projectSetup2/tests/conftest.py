"""This module contains pytest fixtures for test setup."""
from decimal import Decimal
import pytest
from calculator.history import History
from calculator.operations import Operations

@pytest.fixture
def sample_calculations():
    """Fixture to add sample calculations to history for testing."""
    History.clear_history()  # Reset history before tests

    calculations = [
        (Decimal(2), "add", Decimal(3), Operations.add(Decimal(2), Decimal(3))),
        (Decimal(10), "subtract", Decimal(4), Operations.subtract(Decimal(10), Decimal(4))),
        (Decimal(5), "multiply", Decimal(5), Operations.multiply(Decimal(5), Decimal(5))),
        (Decimal(20), "divide", Decimal(5), Operations.divide(Decimal(20), Decimal(5)))
    ]

    for calc in calculations:
        History.add_calculation(*calc)

    return calculations  #Return sample calculations if needed in tests
