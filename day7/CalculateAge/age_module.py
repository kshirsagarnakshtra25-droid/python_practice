from datetime import datetime

def calculate_age():
    birth_year = int(input("Enter your Birth Year: "))

    current_year = datetime.now().year

    age = current_year - birth_year

    print("Approximate Age:", age)