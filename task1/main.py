from datetime import datetime, timedelta

users = [
    {"name": "Winnie the Pooh", "birthday": datetime(2005, 10, 14)},
    {"name": "Christopher Robin", "birthday": datetime(2005, 10, 15)},
    {"name": "Piglet", "birthday": datetime(2006, 10, 17)},
    {"name": "Eeyore", "birthday": datetime(2004, 11, 11)},
    {"name": "Kanga", "birthday": datetime(1995, 10, 25)},
    {"name": "Roo", "birthday": datetime(2010, 10, 18)},
    {"name": "Tigger", "birthday": datetime(2004, 9, 18)}
]

week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# get current date
current_date = datetime.today().date()
day_today = datetime.today().weekday()
days_before_monday = 7 - datetime.today().weekday()
week_starts = datetime.today().replace(day=datetime.today().date().day + days_before_monday).date()

def get_birthdays_next_week():
    birthdays = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': [], 'Saturday': [], 'Sunday': []}
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=datetime.today().year)
    
        if birthday_this_year < current_date - timedelta(days=2):
            birthday_this_year = birthday.replace(year=datetime.today().year + 1)

        delta_days = (birthday_this_year - week_starts).days

        if delta_days >=0 and delta_days < 5:
            birthdays[week_days[delta_days]].append(name)
        elif delta_days == -1 or delta_days == -2:
            birthdays[week_days[0]].append(name)
  
    print_birthdays(birthdays)


def print_birthdays(birthdays):
   for day, names in birthdays.items():
        if names:
            print(f"{day}: {', '.join(names)}")
     

def get_birthdays_per_week():
    birthdays = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': [], 'Saturday': [], 'Sunday': []}
    day_today = datetime.today().weekday()
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=datetime.today().year)
        
        if birthday_this_year < current_date:
            birthday_this_year = birthday.replace(year=datetime.today().year + 1)

        delta_days = (birthday_this_year - datetime.today().date()).days
        if delta_days < 7:
            day_number = (day_today+delta_days)%7
            if day_number > 0 and day_number < 5:
                birthdays[week_days[day_number]].append(name)
            else:
                birthdays[week_days[0]].append(name)
      
    i = day_today
    while i < 5:
        arr = birthdays[week_days[i]]
        if arr:
            print(f"{week_days[i]}: {', '.join(arr)}")
        i+=1
    
    i = 0
    while i < day_today:
        arr = birthdays[week_days[i]]
        if arr:
            print(f"{week_days[i]}: {', '.join(arr)}")
        i+=1
    

def main():
    print('-- Today is ',current_date, '. It is ', week_days[day_today], '---' )
    get_birthdays_next_week()
    print('---------------------')
    get_birthdays_per_week()
    print('---------------------')

if __name__ == "__main__":
    main()