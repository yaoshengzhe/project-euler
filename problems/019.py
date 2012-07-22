#! /usr/bin/python

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
accumulate_month_days = [ sum(month_days[:(i+1)]) for i in range(len(month_days))]
#print accumulate_month_days
def is_leap_year(year):
    if year % 100 == 0:
        return year % 400 == 0
    else:
        return year % 4 == 0

def is_sunday(year, month, day):
    if year < 1900:
        raise Exception("Sorry, I don't know... Year is less than 1900.")

    days_in_year = accumulate_month_days[month-1] + day
    if month > 2 and is_leap_year(year):
        days_in_year += 1

    days_to_1900 = (year - 1900) * 365
    days_to_1900 += (year+3)/4 - (1900+3)/4
    days_to_1900 -= (year+399)/400 - 5
    days_to_1900 += days_in_year

    return days_to_1900 % 7 == 0

def foo():
    num_of_sunday = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            if is_sunday(year, month, 1):
                num_of_sunday += 1
    return num_of_sunday

def main():
    print foo()

if __name__ == '__main__':
    main()
