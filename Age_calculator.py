from datetime import date
from dateutil.relativedelta import relativedelta

def calculate_age(day, month, year):
    today = date.today()
    birthdate = date(year, month, day)

    diff = relativedelta(today, birthdate)

    return diff.years, diff.months, diff.days

if __name__ == "__main__":
    try:
        day = int(input("Enter day: "))
        month = int(input("Enter month: "))
        year = int(input("Enter year: "))

        years, months, days = calculate_age(day, month, year)

        print(f"You are {years} years, {months} months, and {days} days old")

    except:
        print("Invalid date entered")
