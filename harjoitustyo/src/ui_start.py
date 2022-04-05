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

        amount_of_moults = int(input("Anna jäljelläolevien nahanluontien määrä: "))
        frequency_of_moults = int(input("Anna arvioitu nahanluontien taajuus päivinä: "))

        change = input("Muuta aikaa viimeiselle nahanluonnille ennen aikuisuutta? [y/n] ")

        if change == "y":
            last_moult = int(input("Juveniili -> Aikuinen -kesto päivinä: "))
            result = Calculator.calculate(amount_of_moults, frequency_of_moults, last_moult)

        elif change == "n":
            last_moult = 0
            result = Calculator.calculate(amount_of_moults, frequency_of_moults, last_moult)

        print(f"Arvioitu aikuistuminen tapahtuu {result} päivän kuluttua")
