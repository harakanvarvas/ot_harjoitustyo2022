from calculator import Calculator

class UiStart:

    def __init__(self):
        self.commands = {
            "1": "Tee uusi arvio selkärangattoman aikuistumisesta",
            "2": "Lopeta"
        }
        self.amount = 0
        self.frequency = 0
        self.last = 0

    def start(self):

        while True:

            for command, explanation in self.commands.items():
                print(command, explanation)

            command = input("Anna komennon numero: ")

            if command not in self.commands:
                print("Virheellinen komento")
            if command == "2":
                print("Suljetaan sovellus")
                break
            if command == "1":
                UiStart.amount_of_moults(self)


    def amount_of_moults(self):
        while True:
            amount = input("Anna jäljelläolevien nahanluontien määrä: ")
            try:
                self.amount = int(amount)
            except ValueError:
                print("Virhe: Määrän tulee olla positiivinen kokonaisluku")
                continue

            if amount < 1:
                print("Virhe: Määrä ei voi olla pienempi kuin 1")
                continue

            break
        UiStart.frequency_of_moults(self)

    def frequency_of_moults(self):
        while True:
            frequency = input("Anna arvioitu nahanluontien taajuus päivinä: ")
            try:
                self.frequency = int(frequency)
            except ValueError:
                print("Virhe: Taajuuden tulee olla positiivinen kokonaisluku")
                continue

            if frequency < 0:
                print("Virhe: Taajuus ei voi olla negatiivinen")
                continue

            break
        UiStart.change(self)

    def change(self):
        while True:
            change = input("Muuta aikaa ennen viimeistä nahanluontia? (y/n) ")
            if change.lower() == "y" or change.lower() == "n":
                break
            print("Virhe: Merkki ei ole vaihtoehdoissa")

        if change.lower() == "y":
            while True:
                last = input("Kesto päivinä: ")
                try:
                    self.last = int(last)
                except ValueError:
                    print("Virhe: Keston tulee olla annettu positiivisena kokonaislukuna")
                    continue

                if int(last) < 0:
                    print("Virhe: Kesto ei voi olla negatiivinen")
                    continue

                break

        result = Calculator.calculate(self.amount, self.frequency, self.last)

        if result >= 7:
            weeks = Calculator.weeks(result)
            print(f"Aikuistuminen tapahtuu arviolta {weeks[0]} viikon kuluttua, viikolla {weeks[1]}")
        else:
            print(f"Aikuistuminen tapahtuu arviolta {result} päivän kuluttua")