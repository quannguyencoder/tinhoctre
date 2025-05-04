def is_leap(year):
    if (year % 4 == 0) and not (year % 100 == 0) or (year % 400):
        is_leap = ("True")
    else:
        is_leap = ("False")
        print (is_leap)

year = int(input())
print(is_leap(year))