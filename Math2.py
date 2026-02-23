year=int(input("Enter the year:"))
month=int(input("Enter the month:"))
day=int(input("Enter the day:"))
cuyear=int(input("Enter the current year:"))
cumonth=int(input("Enter the current month:"))
cuday=int(input("Enter the current day:"))

age = cuyear-year
if cumonth<month or (cumonth==month and cuday<day):
    age-=1
print("Your age is:",age)