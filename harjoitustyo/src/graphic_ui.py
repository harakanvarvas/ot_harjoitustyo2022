from calculator import Calculator
from tkinter import Tk, ttk, constants, END
from tkcalendar import Calendar


class GraphicUI:
    def __init__(self, root):
        self._root = root
        self._entry_amount = None
        self._entry_frequency = None
        self._entry_last = None
        self._result_label = None
        self._calculator = Calculator()

    def start(self):
        heading_label = ttk.Label(master=self._root, text="LASKIN")
        amount_label = ttk.Label(master=self._root, text="Muodonvaihdosten määrä:")
        self._entry_amount = ttk.Entry(master=self._root)
        frequency_label = ttk.Label(master=self._root, text="Muodonvaihdosten taajuus:")
        self._entry_frequency = ttk.Entry(master=self._root)
        optional_label = ttk.Label(master=self._root, text="(Valinnainen)   ")
        last_label = ttk.Label(master=self._root, text="Viimeisen muodonvaihdoksen kesto:")
        self._entry_last = ttk.Entry(master=self._root)
        calculate = ttk.Button(master=self._root, text="Laske", command=self._handle_calculate_click)
        clear = ttk.Button(master=self._root, text="Tyhjennä", command=lambda : self._handle_clear_click(self._result_label))
        calendar = Calendar(master=self._root, setmode="day", date_pattern="d/m/yy")

        heading_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        amount_label.grid(row=1, column=0, sticky=constants.E, padx=10, pady=10)
        self._entry_amount.grid(row=1, column=1, sticky=constants.W)
        frequency_label.grid(row=2, column=0, sticky=constants.E, padx=10, pady=10)
        self._entry_frequency.grid(row=2, column=1, sticky=constants.W)
        optional_label.grid(row=3, column=0, sticky=constants.E)
        last_label.grid(row=4, column=0, sticky=constants.E, padx=10)
        self._entry_last.grid(row=4, column=1, sticky=constants.W)
        calculate.grid(row=5, column=0, columnspan=2, padx=10, pady=20)
        clear.grid(row=5, column=1, columnspan=2, sticky=constants.W, padx=80)
        calendar.grid(row=7, column=1, sticky=constants.W, pady=20)

        self._root.grid_columnconfigure(0, weight=1)
        self._root.grid_columnconfigure(1, weight=1, minsize=250)

    def _handle_calculate_click(self):
        try:
            self._result_label.destroy()
        except:
            AttributeError
        entry_amount = self._entry_amount.get()
        entry_frequency = self._entry_frequency.get()
        entry_last = self._entry_last.get()
        print(entry_last)

        calculated = self._calculator.calculate(entry_amount, entry_frequency, entry_last)

        self._result_label = ttk.Label(master=self._root, text=f"{calculated}")
        self._result_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
    
    def _handle_clear_click(self, label):
        self._entry_amount.delete(0, END)
        self._entry_frequency.delete(0, END)
        self._entry_last.delete(0, END)
        self._result_label.destroy()




window = Tk()
window.title("Molttilaskin")

ui = GraphicUI(window)
ui.start()

window.mainloop()