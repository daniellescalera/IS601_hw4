# pylint: disable=missing-module-docstring, missing-function-docstring
"""Tests for the History class."""
from calculator.history import History

def test_add_and_retrieve_calculation(sample_calculations):
    """Test adding calculations to history and retrieving the last one."""
    last_calc = History.get_last_calculation()
    assert last_calc is not None  # History should not be empty
    assert last_calc == sample_calculations[-1]  # Last added should be last retrieved

def test_clear_history(sample_calculations):  # pylint: disable=unused-argument
    """Tests clearing the calculation history."""
    History.clear_history()
    assert not History.get_all_history()  #Checks if history is empty
