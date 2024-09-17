import datetime, bday_messages

today = datetime.date.today()

next_birthday = datetime.date(2024, 10, 25)

time_difference = next_birthday - today  

days_away = time_difference.days

if today == next_birthday:
    print(bday_messages.bday_messages)
else:
    print(f'My next birthday is {days_away} days away!')