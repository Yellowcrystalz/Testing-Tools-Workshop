Feature: Calculator

    Scenario: Adding two numbers
        Given I have a calculator
        When I add 10 and 5
        Then the result should be 15

    Scenario: Subtracting two numbers
        Given I have a calculator
        When I subtract 10 and 5
        Then the result should be 5

    Scenario: Multiplying two numbers
        Given I have a calculator
        When I multiply 10 and 5
        Then the result should be 50

    Scenario: Dividing two numbers
        Given I have a calculator
        When I divide 10 and 5
        Then the result should be 2