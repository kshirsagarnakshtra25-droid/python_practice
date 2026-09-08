from datetime import datetime, date

def days_remaining():
    future_date = input("Enter Future Date (DD-MM-YYYY): ")

    future = datetime.strptime(future_date, "%d-%m-%Y").date()

    today = date.today()

    days = (future - today).days

    if days > 0:
        print("Days Remaining:", days)
    elif days == 0:
        print("The date is today.")
    else:
        print("The date has already passed.")