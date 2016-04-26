'''
Author: Josh Vocal
Description: Write a program that accepts a year as input and outputs the century the belongs in and
whether or not the year is a leap year.
Version 1.0
Changes:
'''
#Functions
#Leap year algorithm from wikipedia
def ifLeapYear(year):
    if (year % 4 != 0):
        print ("Leap Year: No")
    elif (year % 100 != 0):
        print ("Leap Year: Yes")
    elif (year % 400 != 0):
        print ("Leap Year :Yes")

def whatCentury(year):
    century = (year + 99)/100
    print ("Century: %d") % (century)

#Main
year = input("Enter year: ")
ifLeapYear(year)
whatCentury(year)

