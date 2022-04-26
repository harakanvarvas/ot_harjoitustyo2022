from ot_calendar import CalendarOT

class Calculator:
    def __init__(self):
        self._result = None

    def calculate(self, amount, frequency, last):
#tarkistetaan, että määrä on luku ja suurempi kuin 1
        valid_amount = Calculator.check_value_amount(self, amount)
        if valid_amount == False:
            self._result = Calculator.error_message_invalid_amount(self)
            return self._result

#tarkistetaan, että taajuus in luku ja suurempi kuin 0
        valid_frequency = Calculator.check_value_frequency(self, frequency)
        if valid_frequency == False:
            self._result = Calculator.error_message_invalid_frequency(self)
            return self._result

#tarkistetaan, onko viimeiselle annettu arvoa, ja jos on, että se on luku ja nolla tai suurempi
        valid_last = Calculator.check_value_last(self, last)
        if valid_last == False:
            self._result = Calculator.error_message_invalid_last(self)
            return self._result

#varsinainen laskutoimitus
        if valid_last == None or valid_last == 0:
            self._result = valid_amount * valid_frequency
        elif valid_amount == 1:
            return f"Aikuistuminen tapahtuu arviolta {valid_last} päivän kuluttua"
        else:
            self._result = (valid_amount - 1) * valid_frequency + valid_last

        result = Calculator.returning_the_result(self)
        return result

    def returning_the_result(self):
        if self._result >= 7:
            weeks = Calculator.weeks(self._result)
            return f"Aikuistuminen tapahtuu arviolta {weeks[0]} viikon kuluttua, viikolla {weeks[1]}"
        else:
            return f"Aikuistuminen tapahtuu arviolta {self._result} päivän kuluttua"


#validin määrän tarkistaminen
    def check_value_amount(self, amount):
        try:
            amount = int(amount)
        except ValueError:
            return False

        if int(amount) < 1:
            return False
        return int(amount)

#validin taajuuden tarkistaminen
    def check_value_frequency(self, frequency):
        try:
            frequency = int(frequency)
        except ValueError:
            return False

        if int(frequency) < 0:
            return False
        return int(frequency)

#validin viimeisen tarkistaminen
    def check_value_last(self, last):
        if last == "":
            return None
        else:
            try:
                last = int(last)
            except ValueError:
                return False

            if int(last) < 0:
                return False
            return int(last)

#virheilmoitukset
    def error_message_invalid_amount(self):
        return f"Virhe: Määrän tulee olla kokonaisluku, eikä luku voi olla pienempi kuin 1"

    def error_message_invalid_frequency(self):
        return f"Virhe: Taajuuden tulee olla kokonaisluku, eikä luku voi olla pienempi kuin 0"
    
    def error_message_invalid_last(self):
        return f"Virhe: Viimeisen tulee olla kokonaisluku, eikä luku voi olla pienempi kuin 0"


    def weeks(self, days):
        weeks = days // 7
        maturing_week = CalendarOT.maturing_week(days)
        return (weeks, maturing_week)
