# calculator/__init__.py

# Import specific components but avoid circular imports
from .operations import Operations
from .calculations import Calculation
from .history import History

# Define what is available when importing the calculator package
__all__ = ["Operations", "Calculation", "history"]
