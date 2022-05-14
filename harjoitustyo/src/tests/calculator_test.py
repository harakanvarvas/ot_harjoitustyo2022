"""Tiedosto laskimen testeille"""
import unittest
from datetime import datetime
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    """Testiluokka laskimelle"""
    def setUp(self):
        """Alustetaan laskin"""
        self.calculator = Calculator()

    def test_valid_amount_returns_error(self):
        """ohjelma palauttaa virheen, kun määrä on negatiivinen"""
        self.assertEqual(self.calculator.calculate(-1, 1, 1), "Virhe: Määrän tulee olla kokonaisluku, eikä luku voi olla pienempi kuin 1")

    def test_valid_frequency_returns_error(self):
        """palauttaa virheen, kun taajuus on negatiivinen"""
        self.assertEqual(self.calculator.calculate(1, -1, 1), "Virhe: Taajuuden tulee olla kokonaisluku, eikä luku voi olla pienempi kuin 0")

    def test_calculator_returns_result_when_last_has_no_value(self):
        """tarkistaa, että ohjelma toimii, kun viimeiselle ei anneta erillistä arvoa"""
        self.assertEqual(self.calculator.calculate(1, 1, ""), "Aikuistuminen arviolta 1 päivän kuluttua")

    def test_valid_last_returns_error(self):
        """palauttaa virheen, kun viimeinen on negatiivinen"""
        self.assertEqual(self.calculator.calculate(1, 1, -1), "Virhe: Viimeisen tulee olla kokonaisluku, eikä luku voi olla pienempi kuin 0")

    def test_calculate_returns_amount_error_message(self):
        """määrän virheviesti palautuu"""
        self.assertEqual(self.calculator.calculate(-1, 1, 0), "Virhe: Määrän tulee olla kokonaisluku, eikä luku voi olla pienempi kuin 1")

    def test_calculate_returns_frequency_error_message(self):
        """taajuuden virheviesti palautuu"""
        self.assertEqual(self.calculator.calculate(1, -1, 0), "Virhe: Taajuuden tulee olla kokonaisluku, eikä luku voi olla pienempi kuin 0")

    def test_calculate_returns_last_error_message(self):
        """viimeisen virheviesti palautuu"""
        self.assertEqual(self.calculator.calculate(1, 1, -1), "Virhe: Viimeisen tulee olla kokonaisluku, eikä luku voi olla pienempi kuin 0")

    def test_calculator_works(self):
        """normaalin toiminnan testaaminen"""
        self.assertEqual(self.calculator.calculate(1, 1, 1), "Aikuistuminen tapahtuu arviolta 1 päivän kuluttua")

    def test_calculator_returns_the_result_when_all_the_variables_equal_zero(self):
        """tarkistaa toiminnan kaikkien lukujen ollessa 0"""
        result = self.calculator.calculate(0, 0, 0)
        self.assertEqual(result, "Virhe: Määrän tulee olla kokonaisluku, eikä luku voi olla pienempi kuin 1")

    def test_calculator_returns_the_result_when_amount_equals_zero(self):
        """tarkistaa virheilmoituksen palautumisen määrän ollessa 0"""
        result = self.calculator.calculate(0, 1, 1)
        self.assertEqual(result, "Virhe: Määrän tulee olla kokonaisluku, eikä luku voi olla pienempi kuin 1")

    def test_calculator_returns_the_result_when_all_the_variables_are_negative(self):
        """virheilmoituksen palautuminen kaikkien arvojen ollessa 0"""
        result = self.calculator.calculate(-1, -1, -1)
        self.assertEqual(result, "Virhe: Määrän tulee olla kokonaisluku, eikä luku voi olla pienempi kuin 1")

    def test_calculator_returns_the_result_when_amount_is_more_than_one(self):
        """palauttaa tuloksen määrän ollessa suurempi kuin 1"""
        result = self.calculator.calculate(2, 1, 1)
        self.assertEqual(result, "Aikuistuminen arviolta 2 päivän kuluttua")
