from calendar import Calendar

class Calculator:
    def __init__(self):
#        self._last = None
#        self._amount = None
#        self._frequency = None
        self._result = None

    def calculate(self, amount, frequency, last):

        valid_amount = Calculator.check_value_amount(self, amount)
        if valid_amount == False:
            self._result = Calculator.error_message_invalid_amount(self)
            return self._result

        valid_frequency = Calculator.check_value_frequency(self, frequency)
        if valid_frequency == False:
            self._result = Calculator.error_message_invalid_frequency(self)
            return self._result
        
        valid_last = Calculator.check_value_last(self, last)
        if valid_last == False:
            self._result = Calculator.error_message_invalid_amount(self)
            return self._result

        if last == 0:
            self._result = amount * frequency
        elif valid_amount < 0 or frequency < 0 or last < 0:
            return False
        elif valid_amount == 1:
            return last
        else:
            self._result = (valid_amount - 1) * frequency + last

        return self._result

    def check_value_amount(self, amount):
        try:
            amount = int(amount)
        except ValueError:
            return False

        if int(amount) < 1:
            return False
        return int(amount)

    def check_value_frequency(self, frequency):
        try:
            frequency = int(frequency)
        except ValueError:
            return False

        if int(frequency) < 1:
            return False
        return int(frequency)

    def check_value_last(self, last):
        if last != None:
            try:
                last = int(last)
            except ValueError:
                return False

            if int(last) < 1:
                return False
            return int(last)


    def error_message_invalid_amount(self):
        return f"Virhe: Määrän tulee olla kokonaisluku, eikä luku voi olla pienempi kuin 1"

    def error_message_invalid_frequency(self):
        return f"Virhe: Taajuuden tulee olla kokonaisluku, eikä luku voi olla pienempi kuin 0"


    def weeks(days):
        weeks = days // 7
        maturing_week = Calendar.maturing_week(days)
        return (weeks, maturing_week)
