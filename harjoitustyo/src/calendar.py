"""Kalenteriin merkittyjen aikuistumisten näyttämisen ja poistamisen hoitava luokka"""
from tkinter import tk
from tkcalendar import Calendar

def open_file():
    with open("events.csv") as datafile:
        contents = datafile.read()
    return contents

class EventCalendar(Calendar):
    def __init__(self):
        self._events = open_file()