# Leap Year Rules: How to Calculate Leap Years
# In our modern-day Gregorian calendar, three criteria must be
# taken into account to identify leap years:
# The year must be evenly divisible by 4;
# If the year can also be evenly divided by 100, it is not a leap year;
# unless...
# The year is also evenly divisible by 400. Then it is a leap year.

def leap_year(prompt):
    """
    Asks for the year and returns whether it is a leap year or not
    """
    while True:
        try:
            year_input = int(input(prompt))
            if (year_input % 4 == 0 and year_input % 100 != 0) or (year_input % 400 == 0):
                return "It's a leap year!"
            else:
                return "Isn't a leap year!"
        except ValueError:
            print("Only integer numbers are allowed in year!")
    
if __name__=="__main__":
    
    year = leap_year("Enter a year to check whether it is a leap year or not: ")
    print(year)
    


# def leap_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         leap = "It's a leap year"
#     else:
#         leap = "Isn't a leap year"
#     return leap

# year = int(input("Enter year: "))
# print(leap_year(year))

"""
1 year % 4 == 0: Checks if the year is divisible by 4. If not, it cannot be a leap year.
2 year % 100 != 0: If the year is divisible by 4, 
# it must not be divisible by 100 unless the next condition applies.
3 year % 400 == 0: If the year is divisible by 100, it must also be divisible by 400 to be a leap year.
4 The logical or combines the two conditions. A year is a leap year if it satisfies either:
# Divisible by 4 and not divisible by 100, OR
# Divisible by 400.
"""