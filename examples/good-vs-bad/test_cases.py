def test_example():
    #! Example A
    assert add(10,5)==15 and subtract(10,5)==5 and multiply(10,5)==50 and divide(10,5)==2

    #* Example B
    assert add(10, 5) == 15
    assert subtract(10, 5) == 5
    assert multiply(10, 5) == 50
    assert divide(10, 5) == 2

    #! Example A
    assert string is not None
    assert string != ""
    assert string == "I like ducks"

    #* Example B
    assert string == "I like ducks"

    #* Example A
    calc = Calculator()
    result = calc.add(2, 3)
    assert result == 5

    #! Example B
    assert Calculator().add(2, 3)
