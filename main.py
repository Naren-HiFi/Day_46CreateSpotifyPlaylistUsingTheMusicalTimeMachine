from datetime import datetime
import re
import requests

user_input = input("what year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')

if date_pattern.match(user_input):
    try:
        date_object = datetime.strptime(user_input, '%Y-%m-%d')
        formatted_date = date_object.strftime("%Y-%m-%d")
    except ValueError:
        print("Invalid date format!")
else:
    print("Invalid input format. Please use YYYY-MM-DD format.")
