import unittest
from calculator import Calculator
from ot_calendar import CalendarOT

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_valid_amount_returns_error(self):
        self.assertEqual(self.calculator.check_value_amount(-1), False)

    def test_valid_amount_returns_no_error(self):
        self.assertEqual(self.calculator.check_value_amount(1), 1)

    def test_valid_frequency_returns_error(self):
        self.assertEqual(self.calculator.check_value_frequency(-1), False)

    def test_valid_frequency_returns_no_error(self):
        self.assertEqual(self.calculator.check_value_frequency(1), 1)

    def test_valid_last_returns_none(self):
        self.assertEqual(self.calculator.check_value_last(""), None)

    def test_valid_last_returns_error(self):
        self.assertEqual(self.calculator.check_value_last(-1), False)

    def test_valid_last_returns_no_error(self):
        self.assertEqual(self.calculator.check_value_last(1), 1)

    def test_calculator_works_when_last_equals_zero(self):
        self.assertEqual(self.calculator.calculate(1, 1, 0), "1")

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