import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_calculator_works_when_last_equals_zero(self):
        self.assertEqual(str(Calculator.calculate(1, 1, 0)), "1")

    def test_calculator_works(self):
        self.assertEqual(str(Calculator.calculate(1, 1, 1)), "1")

    def test_calculator_returns_the_result_when_last_equals_zero(self):
        result = Calculator.calculate(1, 1, 0)
        self.assertEqual(str(result), "1")

    def test_calculator_returns_the_result(self):
        result = Calculator.calculate(1, 1, 1)
        self.assertEqual(str(result), "1")
