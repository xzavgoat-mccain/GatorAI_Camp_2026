# Program to get user's birthday and calculate age in days

from datetime import datetime, date

birthday_input = input("Enter your birthday (YYYY-MM-DD): ")

try:
    birthday = datetime.strptime(birthday_input, "%Y-%m-%d").date()
except ValueError:
    print("Invalid date format. Please use YYYY-MM-DD.")
else:
    today = date.today()

    if birthday > today:
        print("Your birthday cannot be in the future.")
    else:
        age_in_days = (today - birthday).days
        print(f"You are {age_in_days} days old.")