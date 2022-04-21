from tkinter import Tk, ttk, constants

class GraphicUI:
    def __init__(self, root):
        self._root = root

    def start(self):
        heading_label = ttk.Label(master=self._root, text="LASKIN")
        amount_label = ttk.Label(master=self._root, text="Muodonvaihdosten määrä:")
        amount_entry = ttk.Entry(master=self._root)
        frequency_label = ttk.Label(master=self._root, text="Muodonvaihdosten taajuus:")
        frequency_entry = ttk.Entry(master=self._root)
        optional_label = ttk.Label(master=self._root, text="(Valinnainen)   ")
        last_label = ttk.Label(master=self._root, text="Viimeisen muodonvaihdoksen kesto:")
        last_entry = ttk.Entry(master=self._root)
        button = ttk.Button(master=self._root, text="Laske")

        heading_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        amount_label.grid(row=1, column=0, sticky=constants.E, padx=10, pady=10)
        amount_entry.grid(row=1, column=1, sticky=constants.W)
        frequency_label.grid(row=2, column=0, sticky=constants.E, padx=10, pady=10)
        frequency_entry.grid(row=2, column=1, sticky=constants.W)
        optional_label.grid(row=3, column=0, sticky=constants.E)
        last_label.grid(row=4, column=0, sticky=constants.E, padx=10)
        last_entry.grid(row=4, column=1, sticky=constants.W)
        button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        self._root.grid_columnconfigure(0, weight=1)
        self._root.grid_columnconfigure(1, weight=1)

window = Tk()
window.title("Molttilaskin")

ui = GraphicUI(window)
ui.start()

window.mainloop()