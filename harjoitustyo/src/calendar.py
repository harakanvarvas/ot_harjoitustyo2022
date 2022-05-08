"""Kalenteriin merkittyjen aikuistumisten näyttämisen ja poistamisen hoitava luokka"""
from tkinter import tk
from tkcalendar import Calendar

def open_file():
"""Avaa ja lukee tapahtumatiedoston myöhempää käyttöä varten"""
    with open("events.csv") as datafile:
        contents = datafile.read()
    return contents

class EventCalendar(Calendar):
"""Tapahtumakalenterin luokka kalenteritapahtumien käsittelyyn"""
    def __init__(self, root):
        self._root = root
        self._events = open_file()

    def calendar(self):
        """luo kalenterin"""
        calendar = Calendar(master=self._root, setmode="day", date_pattern="d/m/yy")#tarkista kalenterikuukausi laskimen tuloksesta
