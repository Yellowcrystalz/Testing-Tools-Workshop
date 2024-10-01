import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from calculator import Calculator

scenarios("calculator.feature")

@given("I have a calculator", target_fixture="calculator")
def calculator():
    return Calculator()

@when(parsers.parse("I add {a:d} and {b:d}"), target_fixture="result")
def add(calculator, a, b):
    return calculator.add(a, b)

@when(parsers.parse("I subtract {a:d} and {b:d}"), target_fixture="result")
def subtract(calculator, a, b):
    return calculator.subtract(a, b)

@when(parsers.parse("I multiply {a:d} and {b:d}"), target_fixture="result")
def multiply(calculator, a, b):
    return calculator.multiply(a, b)

@when(parsers.parse("I divide {a:d} and {b:d}"), target_fixture="result")
def divide(calculator, a, b):
    return calculator.divide(a, b)

@then(parsers.parse("the result should be {expected_result:d}"))
def check_result(result, expected_result):
    assert result == expected_result