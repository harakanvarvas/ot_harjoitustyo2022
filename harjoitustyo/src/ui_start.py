
class UI_start:

    def __init__(self):
        self.commands = {
            "1": "Tee uusi arvio selkärangattoman aikuistumisesta",
            "2": "Lopeta"
        }

    def start(self):
        for command in self.commands:
            print(command)
        while True:
            command = input("Anna komento:")
            if command == "2":
                break
