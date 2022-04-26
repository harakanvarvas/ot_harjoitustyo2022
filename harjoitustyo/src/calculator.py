from calendar import Calendar

class Calculator:
    def __init__(self):
#        self._last = None
#        self._amount = None
#        self._frequency = None
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
            return valid_last
        else:
            self._result = (valid_amount - 1) * valid_frequency + valid_last

        return self._result

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
        maturing_week = Calendar.maturing_week(days)
        return (weeks, maturing_week)
