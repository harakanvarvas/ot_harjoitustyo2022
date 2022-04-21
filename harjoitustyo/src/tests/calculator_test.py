import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_calculator_works_when_last_equals_zero(self):
        self.assertEqual(str(Calculator.calculate(1, 1, 0)), "1")

    def test_calculator_works(self):
        self.assertEqual(Calculator.calculate(1, 1, 1), 1)

    def test_calculator_returns_the_result_when_last_equals_zero(self):
        result = Calculator.calculate(1, 1, 0)
        self.assertEqual(result, 1)

    def test_calculator_returns_the_result(self):
        result = Calculator.calculate(1, 1, 1)
        self.assertEqual(result, 1)

    def test_calculator_returns_the_result_when_all_the_variables_equal_zero(self):
        result = Calculator.calculate(0, 0, 0)
        self.assertEqual(result, 0)

    def test_calculator_returns_the_result_when_amount_equals_zero(self):
        result = Calculator.calculate(0, 1, 1)
        self.assertEqual(result, 0)

    def test_calculator_returns_the_result_when_frequency_equals_zero(self):
        result = Calculator.calculate(1, 0, 1)
        self.assertEqual(result, 1)

    def test_calculator_returns_the_result_when_all_the_variables_are_negative(self):
        result = Calculator.calculate(-1, -1, -1)
        self.assertEqual(result, False)

    def test_calculator_returns_the_result_when_amount_is_negative(self):
        result = Calculator.calculate(-1, 1, 1)
        self.assertEqual(result, False)

    def test_calculator_returns_the_result_when_amount_is_more_than_one(self):
        result = Calculator.calculate(2, 1, 1)
        self.assertEqual(result, 2)