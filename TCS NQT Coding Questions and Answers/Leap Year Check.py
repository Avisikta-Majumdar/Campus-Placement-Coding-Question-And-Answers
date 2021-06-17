'''
Write a Python program, to check whether the given year is a leap year or not
using command line arguments. A leap year is a calendar year containing one additional day (Feb 29th)
added to keep the calendar year synchronized with the astronomical year.
'''
def CheckLeapYearOrNot(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return "{} is leap year".format(year)
            else:
                return "{} is not leap year".format(year)
        else:
            return "{} is leap year".format(year)
    else:
        return "{} is not leap year".format(year)



for i in range(int(input("Testcase:-"))):
    year = int(input())
    print(CheckLeapYearOrNot(year))
