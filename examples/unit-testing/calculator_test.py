# calculator_test
import pytest

from calculator_code import Calculator
import pytest

# Test Class for calculator
class CalculatorTester:

    @pytest.fixture
    def calculator(self):
        return Calculator()
    
    # First Test
    # UnitTest 
    def test_add(self, calculator):
        assert calculator.add(3, 4) == 7

    def test_subtract(self, calculator):
        assert calculator.subtract(10, 5) == 10

    def test_multiply(self, calculator):
        assert calculator.multiply(8, 8) == 64

    def test_divide(self, calculator):
        assert calculator.divide(100, 25) == 4

    def test_divide_zero(self, calculator):
        with pytest.raises(ValueError, match = "Cannot divide by zero"):
            calculator.divide(9, 0)

    # Second Test
    # MockTest
    from faker import Faker
    fake = Faker() 

    def test_add_mock(self, mocker, calculator):
        # this makes the result increrase by 100. 
        mocker.patch.object(calculator, "add", return_value = 100)

    # Third Test
    # Faker Test