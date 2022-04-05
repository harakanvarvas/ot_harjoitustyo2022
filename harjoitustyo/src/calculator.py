

class Calculator:

    def calculate(amount, frequency, last):

        if last == 0:
            result = amount * frequency

        else:
            result = (amount - 1) * frequency + last

        return result
