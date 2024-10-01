# Test_pytest.py

from ast import FormattedValue
from logging import Formatter
from unittest import result
import pytest
from calculator import Calculator
from advanced_calculator import AdvancedCalculator
from result_formatter import ResultFormatter
from history_manager import HistoryManager

@pytest.fixture
def setup_system():
    calculator = Calculator()
    advanced_calculator = AdvancedCalculator()
    formatter =ResultFormatter()
    history = HistoryManager()
    return calculator,advanced_calculator,formatter,history

def test_basic_operations(setup_system) :
    calculator,_,formatter,history =setup_system
    # Test addition and formatting
    result = calculator.add(5,3)  
    formatted_result =formatter.format_result("5 + 3", result)
    assert formatted_result == "The result of 5 + 3 is: 8"

    # add result to history
    history.add_to_history("5 + 3", result)
    assert history.get_history() == ["5 + 3 = 8"]

def test_advanced_operations(setup_system):
    _,advanced_calculator,formatter,history =setup_system


    #test power operattion

    result = advanced_calculator.power(2,3)
    formatted_result= formatter.format_result("2^3",result)
    assert formatted_result  == "The result of 2^3 is: 8"

    #add to history 

    history.add_to_history("2^3", result)
    assert history.get_history() ==  ["2^3 = 8"]  