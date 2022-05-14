"""Tiedosto kalenterin testeille"""
import unittest
try:
    from calendar import EventCalendar
except:


class TestCalendar(unittest.TestCase):
    """Testiluokka tapahtumakalenterille"""
    def setup(self):
        """Alustetaan kalenteri"""
        self.eventcalendar = EventCalendar(self)

#    def test_show_events(self):
#        self.assertEqual(self.eventcalendar.show_events(), "")