from datetime import datetime, date

def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()

def get_days_from_today(date_string):
    input_date = string_to_date(date_string)
    current_date = date.today()
    days = (input_date - current_date).days
    return days

input_date_string = input("Enter a date (YYYY.MM.DD): ")
days_from_today = get_days_from_today(input_date_string)
print(f"Days from today: {days_from_today}")