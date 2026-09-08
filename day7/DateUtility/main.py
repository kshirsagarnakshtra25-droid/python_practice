import date_utils

print("\n===== DATE UTILITIES =====")

print("Current Date:", date_utils.current_date())

print("Current Time:", date_utils.current_time())

print("Age:", date_utils.calculate_age(2005))

print(
    "Days Between:",
    date_utils.days_between_dates(
        "01-09-2026",
        "10-09-2026"
    )
)