import datetime

user_date = input("Enter date(mm/dd/yyyy): ")
user_date = user_date.split('/')
user_date_month = int(user_date[0])
user_date_day = int(user_date[1])
user_date_year = int(user_date[2])

date = datetime.datetime(user_date_year, user_date_month, user_date_day)
print(date.strftime("%B %d,%Y"))
