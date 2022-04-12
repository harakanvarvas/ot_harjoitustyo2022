

class Calculator:

    def calculate(amount, frequency, last):

        if int(last) == 0:
            result = int(amount) * int(frequency)

        else:
            result = (int(amount) - 1) * int(frequency) + int(last)

        return result
