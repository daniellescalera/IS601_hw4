"""Handles storing and executing a calculation."""

class Calculation:
    """A class to store and execute a calculation."""
    def __init__(self, a, b, operation, result):  # ✅ Order: a, b, operation, result
        self.a = a
        self.b = b
        self.operation = operation
        self.result = result

    def get_result(self):
        """Returns the calculation result."""
        return self.result
