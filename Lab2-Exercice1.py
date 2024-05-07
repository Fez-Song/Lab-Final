import datetime


def days_until_end_of_year():
    today = datetime.date.today()
    end_of_year = datetime.date(today.year, 12, 31)
    days_left = (end_of_year - today).days
    return days_left


days_left = days_until_end_of_year()
print("Number of days until the end of the year:", days_left)
