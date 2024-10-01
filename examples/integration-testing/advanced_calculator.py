# advanced_calculator.py

from math import sqrt

class AdvancedCalculator:
    def power(self, base, exponent):
        return base ** exponent

    def square_root(self, value):
        if value < 0:
            raise ValueError("Cannot take square root of a negative number")
        return sqrt(value)
