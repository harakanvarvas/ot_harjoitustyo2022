from datetime import date, datetime, timedelta

class Calendar:
    def today():
        today = datetime.now()
        return today

#    def formatting_today(date):
#        today = date.strftime("%d.%m.%Y")
#        return today

    def week():
        week = datetime.now().isocalendar()[1]
        return week

    def maturing_week(amount_of_days):
        today = Calendar.today()
        days = timedelta(days=amount_of_days)
        maturing_date = today + days
        maturing_week = maturing_date.isocalendar()[1]
        return maturing_week


#if __name__ == "__main__":
#    print(Calendar.maturing_week(26))

