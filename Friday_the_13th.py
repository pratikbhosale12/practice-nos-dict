#Write a function to detect 13th Friday. The function can accept two parameters, and both will be numbers.
# The first parameter will be the number indicating the month, and the second will be the year in four
# digits. Your function should parse the parameters, and it must return True when the month contains a
# Friday with the 13th, else return False.
from datetime import date

def friday_thirteenth(month,year):
    if date(year,month,13).weekday() == 4:
        return True
    else:
        return False

month = int(input("Enter Month as MM:"))
year = int(input("Enter Year as YYYY:"))

check = friday_thirteenth(month,year)
if check == True:
    print("13 /",month,"/",year," falls on a Friday")
else:
    print("13 /",month,"/",year," does not fall on a Friday")


