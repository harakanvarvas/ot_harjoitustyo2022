"""Tiedosto muodonvaihdoslaskutoimimtuksia varten"""
from datetime import date, datetime, timedelta

def error_message_invalid_amount():
    """virheilmoitus väärälle määrälle"""
    return "Virhe: Määrän tulee olla kokonaisluku, eikä luku voi olla pienempi kuin 1"

def error_message_invalid_frequency():
    """virheilmoitus väärälle taajuudelle"""
    return "Virhe: Taajuuden tulee olla kokonaisluku, eikä luku voi olla pienempi kuin 0"

def error_message_invalid_last():
    """virheilmoitus väärälle viimeisen arvolle"""
    return "Virhe: Viimeisen tulee olla kokonaisluku, eikä luku voi olla pienempi kuin 0"

def check_today():
    """tarkistaa päivämäärän"""
    today = date.today()
    return today

def week():
    """tarkistaa kalenteriviikon numeron"""
    week = datetime.now().isocalendar()[1]
    return week

def maturing_week(amount_of_days):
    """laskee aikuistumisviikolle kalenteriviikon"""
    today = check_today()
    days = timedelta(days=amount_of_days)
    maturing_date = today + days
    date = maturing_date.isocalendar()
    maturing_date = (date[0], date[1])
    return maturing_date

def weeks(days):
    """viikkojen määrä"""
    week_amount = days // 7
    maturing = maturing_week(days)
    return (week_amount, maturing[0], maturing[1])

def check_value_amount(amount):
    """validin määrän tarkistaminen"""
    try:
        amount = int(amount)
    except ValueError:
        return False

    if int(amount) < 1:
        return False
    return int(amount)

def check_value_frequency(frequency):
    """validin taajuuden tarkistaminen"""
    try:
        frequency = int(frequency)
    except ValueError:
        return False

    if int(frequency) < 0:
        return False
    return int(frequency)

def check_value_last(last):
    """validin viimeisen tarkistaminen"""
    if last == "":
        return None
    try:
        last = int(last)
    except ValueError:
        return False

    if int(last) < 0:
        return False
    return int(last)

def check_mondays_date(week):
    """Tarkistaa aikuistumisviikon maanantain päivämäärän"""
    pass


class Calculator:
    """laskinluokka"""
    def __init__(self):
        self._result = None

    def calculate(self, amount, frequency, last):
        """laskutoimituksille"""
#tarkistetaan, että määrä on luku ja suurempi kuin 1
        valid_amount = check_value_amount(amount)
        if valid_amount is False:
            self._result = error_message_invalid_amount()
            return self._result

#tarkistetaan, että taajuus in luku ja suurempi kuin 0
        valid_frequency = check_value_frequency(frequency)
        if valid_frequency is False:
            self._result = error_message_invalid_frequency()
            return self._result

#tarkistetaan, onko viimeiselle annettu arvoa, ja jos on, että se on luku ja nolla tai suurempi
        valid_last = check_value_last(last)
        if valid_last is False:
            self._result = error_message_invalid_last()
            return self._result

#varsinainen laskutoimitus
        if valid_last in (None, 0):
            self._result = valid_amount * valid_frequency
        elif valid_amount == 1:
            return f"Aikuistuminen tapahtuu arviolta {valid_last} päivän kuluttua"
        else:
            self._result = (valid_amount - 1) * valid_frequency + valid_last

        result = Calculator.returning_the_result_with_text(self)
        return result

    def returning_the_result_with_text(self):
        """tuloksen palauttaminen"""
        if self._result >= 7:
            week_amount = weeks(self._result)
            return f"Aikuistuminen arviolta {week_amount[0]} viikon kuluttua, vuoden {week_amount[1]} viikolla {week_amount[2]}"
        return f"Aikuistuminen arviolta {self._result} päivän kuluttua"



#if __name__ == "__main__":
#    calc = Calculator()
#    print(calc.check_value_amount(-1))
