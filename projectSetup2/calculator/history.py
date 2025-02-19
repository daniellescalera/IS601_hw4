#this file manages the history of calculations
from typing import List, Tuple, Optional
from decimal import Decimal


class History:
    _history = []  

    @classmethod
    def add_calculation(cls, a, operation, b, result):
        #adds calculation to history
        cls._history.append((a, operation, b, result))

    @classmethod
    def get_last_calculation(cls):
        #returns last calculation if there is one
        return cls._history[-1] if cls._history else None

    @classmethod
    def get_all_history(cls):
        #returns all stored calculations
        return cls._history

    @classmethod
    def clear_history(cls):
        #clears the calculation history
        cls._history.clear()
