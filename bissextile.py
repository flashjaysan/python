# This program says if a year is a leap


def is_leap(year):
    """This function takes a year and returns if it is a leap year.
    Param: year (positive integer)
    Return: boolean
    """
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0


print("Ce programme détermine si une année est bissextile ou non.")
year = input("Saisissez une année : ")

if is_leap(int(year)):
    print("L'année {} est bissextile.".format(year))
else:
    print("L'année {} n'est pas bissextile.".format(year))
