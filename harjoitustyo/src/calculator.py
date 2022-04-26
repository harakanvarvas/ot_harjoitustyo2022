from calendar import Calendar

class Calculator:
    def __init__(self):
        self._last = None
#        self._amount = None
#        self._frequency = None
#        self._result = None

    def calculate(self, amount, frequency, last):

        #self._result = 0

        if last == 0:
            self._result = amount * frequency
        elif amount < 0 or frequency < 0 or last < 0:
            return False
        elif amount == 1:
            return last
        else:
            self._result = (amount - 1) * frequency + last

        return self._result

    def check_values_amount(self, amount):




    def weeks(days):
        weeks = days // 7
        maturing_week = Calendar.maturing_week(days)
        return (weeks, maturing_week)
