from calendar import Calendar

class Calculator:

    def calculate(amount, frequency, last):

        result = 0

        if int(last) == 0:
            result = int(amount) * int(frequency)
        elif int(amount) < 0 or int(frequency) < 0 or int(last) < 0:
            return False
        elif int(amount) == 1:
            return int(last)
        else:
            result = (int(amount) - 1) * int(frequency) + int(last)

        return result

    def weeks(days):
        weeks = days // 7
        maturing_week = Calendar.maturing_week(days)
        return (weeks, maturing_week)
