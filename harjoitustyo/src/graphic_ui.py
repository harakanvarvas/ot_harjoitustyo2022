"""Graafinen käyttöliittymä"""
from tkinter import Tk, ttk, constants, END, Listbox, Scrollbar
#from tkcalendar import Calendar
from calculator import Calculator
#from calendar import EventCalendar

class GraphicUI:
    """Graafisen käyttöliittymän luokka"""
    def __init__(self, root):
        self._root = root
        self._entry_amount = None
        self._entry_frequency = None
        self._entry_last = None
        self._result_label = None
        self._entry_search = None
        self._entry_setdate = None
        self._calculator = Calculator()

    def start(self):
        """funktio rakentaa komponentit ruudulle"""
        heading_label = ttk.Label(master=self._root, text="LASKIN")
        amount_label = ttk.Label(master=self._root, text="Muodonvaihdosten määrä:")
        self._entry_amount = ttk.Entry(master=self._root)
        frequency_label = ttk.Label(master=self._root, text="Muodonvaihdosten taajuus päivinä:")
        self._entry_frequency = ttk.Entry(master=self._root)
        optional_label = ttk.Label(master=self._root, text="(Valinnainen)   ")
        last_label = ttk.Label(master=self._root, text="Viimeisen muodonvaihdoksen kesto päivinä:")
        self._entry_last = ttk.Entry(master=self._root)
        calculate = ttk.Button(master=self._root, text="Laske",
                            command=self._calculate_click)
        clear = ttk.Button(master=self._root, text="Tyhjennä",
                            command=lambda : self._clear_click())
        self._entry_setdate = ttk.Entry(master=self._root)
        set_date = ttk.Button(master=self._root, text="Lisää kalenteriin",
                            command=lambda : self._set_date_click)
        remove_date = ttk.Button(master=self._root, text="Poista kalenterista",
                            command=lambda : self._remove_date_click)
        search = ttk.Button(master=self._root, text="Hae kalenterista",
                            command=lambda : self._search_click)
        self._entry_search = ttk.Entry(master=self._root)
        listbox = Listbox(master=self._root, height=20)
#        scrollbar = Scrollbar(master=listbox)
#        eventcalendar = Calendar(master=self._root, setmode="day", date_pattern="d/m/yy")

        heading_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        amount_label.grid(row=1, column=0, sticky=constants.E, padx=10, pady=10)
        self._entry_amount.grid(row=1, column=1, sticky=constants.W, ipadx=30)
        frequency_label.grid(row=2, column=0, sticky=constants.E, padx=10, pady=10)
        self._entry_frequency.grid(row=2, column=1, sticky=constants.W, ipadx=30)
        optional_label.grid(row=3, column=0, sticky=constants.E)
        last_label.grid(row=4, column=0, sticky=constants.E, padx=10)
        self._entry_last.grid(row=4, column=1, sticky=constants.W, ipadx=30)
        calculate.grid(row=5, column=0, columnspan=2, padx=10, pady=20)
        clear.grid(row=5, column=1, columnspan=2, sticky=constants.W, padx=140)
        set_date.grid(row=7, column=0, columnspan=1, sticky=constants.E, ipadx=20, padx=40, pady=10)
        self._entry_setdate.grid(row=7, column=1, sticky=constants.W, ipadx=58)
#        eventcalendar.grid(row=7, column=1, sticky=constants.W, pady=20)
        search.grid(row=8, column=0, columnspan=1, sticky=constants.E, ipadx=20, padx=40, pady=10)
        self._entry_search.grid(row=8, column=1, sticky=constants.W, ipadx=58)
        listbox.grid(row=9, column=0, rowspan=2, columnspan=2, ipadx=150)
        remove_date.grid(row=13, column=1, columnspan=1, sticky=constants.W, ipadx=13, padx=98, pady=10)


        self._root.grid_columnconfigure(0, weight=1)
        self._root.grid_columnconfigure(1, weight=1, minsize=250)

    def _calculate_click(self):
        """laske-napin painamisen suorittaminen"""
        try:
            self._result_label.destroy()
        except AttributeError:
            False

        calculated = self._calculator.calculate(self._entry_amount.get(), self._entry_frequency.get(), self._entry_last.get())

        self._result_label = ttk.Label(master=self._root, text=f"{calculated}")
        self._result_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def _clear_click(self):
        """Tyhjennä-napin painamisen suorittaminen"""
        self._entry_amount.delete(0, END)
        self._entry_frequency.delete(0, END)
        self._entry_last.delete(0, END)
        self._result_label.destroy()

    def _search_click(self):
        """Hakee kalenterista annetulla hakusanalla"""
        pass

    def _set_date_click(self):
        """Lisää kalenteriin -napin painamisen suorittaminen"""
        pass

    def _remove_date_click(self):
        """Poista kalenterista -napin painamisen suorittaminen"""
        pass


window = Tk()
window.title("Molttilaskin")

ui = GraphicUI(window)
ui.start()

window.mainloop()
