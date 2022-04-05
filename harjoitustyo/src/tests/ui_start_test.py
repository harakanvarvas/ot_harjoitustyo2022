import unittest
from ui_start import UI_start

class TestUI_start(unittest.TestCase):
    def setUp(self):
        self.UI_start = UI_start()

    def test_commands_exist(self):
        self.assertEqual(str(self.UI_start.commands), str("{'1': 'Tee uusi arvio selkärangattoman aikuistumisesta', '2': 'Lopeta'}"))

