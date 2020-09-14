#many attemps later, was sucessfull
#link of sucessfull tutorial: https://stackoverflow.com/questions/28189442/datetime-current-year-and-month-in-python


from datetime import datetime

currentSecond= datetime.now().second
currentMinute = datetime.now().minute
currentHour = datetime.now().hour

currentDay = datetime.now().day
currentMonth = datetime.now().month
currentYear = datetime.now().year

print(currentMonth)