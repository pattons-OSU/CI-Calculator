#! Python 3

"""
Simeon Patton
Test for Calculator App using circle CI
Inclass Activity week 9
OSU CS362 Spring 2021

"""

import calculator


class TestCalculatorApp:
    def test_add(self):
        assert 5 == calculator.add(3, 2)

    def test_subtract(self):
        assert 2 == calculator.subtract(5, 3)

    def test_multiply(self):
        assert 20 == calculator.multiply(10, 2)

    def test_divide(self):
        assert 7 == calculator.divide(14, 2)
