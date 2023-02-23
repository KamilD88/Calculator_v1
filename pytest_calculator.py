from main import Calculator

def test_addition():
    calc = Calculator()
    assert calc.add(2, 3) == 5

def test_subtraction():
    calc = Calculator()
    assert calc.subtract(5, 3) == 2

def test_multiplication():
    calc = Calculator()
    assert calc.multiply(2, 3) == 6

def test_division():
    calc = Calculator()
    assert calc.divide(6, 3) == 2.0
    try:
        calc.divide(6, 0)
        assert False
    except ValueError:
        pass
