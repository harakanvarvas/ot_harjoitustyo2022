from calendar import Calendar

class Calculator:
    def __init__(self):
        self._last = None
        self._amount = None
        self._frequency = None
        self._result = None

    def calculate(amount, frequency, last):

        #self._result = 0

        if int(last) == 0:
            self._result = int(amount) * int(frequency)
        elif int(amount) < 0 or int(frequency) < 0 or int(last) < 0:
            return False
        elif int(amount) == 1:
            return int(last)
        else:
            self._result = (int(amount) - 1) * int(frequency) + int(last)

        return self._result

    def weeks(days):
        weeks = days // 7
        maturing_week = Calendar.maturing_week(days)
        return (weeks, maturing_week)
