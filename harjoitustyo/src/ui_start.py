from calculator import Calculator

class UI_start:

    def __init__(self):
        self.commands = {
            "1": "Tee uusi arvio selkärangattoman aikuistumisesta",
            "2": "Lopeta"
        }

    def start(self):

        while True:

            for command in self.commands:
                print(command, self.commands[command])

            command = input("Anna komento: ")
            if command == "2":
                print("Suljetaan sovellus")
                break
            if command == "1":
                UI_calculator.calculator_start(self)
                
            if command not in self.commands:
                print("Virheellinen komento")


class UI_calculator:

    def calculator_start(self):

        while True:
            amount_of_moults = input("Anna jäljelläolevien nahanluontien määrä: ")
            try:
                amount = int(amount_of_moults)
            except ValueError:
                print("Virhe: Määrän tulee olla positiivinen kokonaisluku")
                continue
                
            if int(amount_of_moults) < 0:
                print("Virhe: Määrä ei voi olla negatiivinen")
                continue

            break

        while True:
            frequency_of_moults = input("Anna arvioitu nahanluontien taajuus päivinä: ")
            try:
                frequency = int(frequency_of_moults)
            except ValueError:
                print("Virhe: Taajuuden tulee olla positiivinen kokonaisluku")
                continue

            if int(frequency_of_moults) < 0:
                print("Virhe: Taajuus ei voi olla negatiivinen")
                continue

            break

        while True:
            change = input("Muuta aikaa viimeiselle nahanluonnille ennen aikuisuutta? (y/n) ")
            if change.lower() == "y" or change.lower() == "n":
                break
            else:
                print("Virhe: Merkki ei ole vaihtoehdoissa")

        if change.lower() == "y":
            while True:
                last_moult = input("Juveniili -> Aikuinen -kesto päivinä: ")
                try: 
                    last = int(last_moult)
                except ValueError:
                    print("Virhe: Keston tulee olla annettu positiivisena kokonaislukuna")
                    continue

                if int(last_moult) < 0:
                    print("Virhe: Kesto ei voi olla negatiivinen")
                    continue

                break

        elif change.lower() == "n":
            last_moult = 0

        result = Calculator.calculate(amount_of_moults, frequency_of_moults, last_moult)

        print(f"Arvioitu aikuistuminen tapahtuu {result} päivän kuluttua")
