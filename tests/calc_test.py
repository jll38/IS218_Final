from calculator import calculator


def test_calc_instance():
    calc = calculator()
    assert isinstance(calc, calculator)

def test_calc_add():
    calc = calculator()
    assert calc.add(1) == 0

def test_calc_sub():
    calc = calculator()
    assert calc.subtract(1) == -1