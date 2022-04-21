import unittest
from text_ui_start import UiStart

class TestUiStart(unittest.TestCase):
    def setUp(self):
        self.ui_start = UiStart()

    def test_commands_exist(self):
        self.assertEqual(str(self.ui_start.commands),
            str("{'1': 'Tee uusi arvio selkärangattoman aikuistumisesta', '2': 'Lopeta'}"))