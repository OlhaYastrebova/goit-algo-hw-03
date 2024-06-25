from datetime import datetime, date

def string_to_date(date_string):
    try:
        return datetime.strptime(date_string, "%Y.%m.%d").date()
    except ValueError:
        print("Incorrect date format, should be YYYY.MM.DD")
        return None

def get_days_from_today(date_string):
    input_date = string_to_date(date_string)
    if input_date is None:
        return "Invalid date format"
    
    current_date = date.today()
    days = (input_date - current_date).days
    return days

# Введення дати користувачем
date_string = input("Enter a date (YYYY.MM.DD): ")

days_from_today = get_days_from_today(date_string)
print(f"Days from today: {days_from_today}")