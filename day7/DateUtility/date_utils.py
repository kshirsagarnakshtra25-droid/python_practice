from datetime import datetime, date


def current_date():
    return date.today().strftime("%d-%m-%Y")


def current_time():
    return datetime.now().strftime("%H:%M:%S")


def calculate_age(birth_year):
    return datetime.now().year - birth_year


def days_between_dates(date1, date2):

    d1 = datetime.strptime(date1, "%d-%m-%Y").date()

    d2 = datetime.strptime(date2, "%d-%m-%Y").date()

    return abs((d2 - d1).days)