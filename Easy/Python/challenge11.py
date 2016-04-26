'''
Author: Josh Vocal
Descripton: Program will talke 3 arguments.  The first will be a day, followed by month, then year.
The program will compute the day of the week that dat will fall on.
Version: 1.0
Changes:
'''
#Imports
import calendar

#Functions
def day():
    print("Pick a day from 1-31 depending on the month: ")
    return input("What is the day? ")

def month():
    print("Janurary = 1\nFeburary = 2\nMarch = 3\nApril = 4\nMay = 5\nJune = 6\nJuly = 7\nAugust = 8\nSeptember = 9\nOctober = 10\nNovember = 11\nDecember = 12")
    return input("What is the month? ")

def year():
    print("Please select a year after 1970")
    return input("What is the year? ")

#Main
#calendary.weekday returns a int depending on what day of the week from 1 -7
weekday = calendar.weekday(year(), month(), day())

if (weekday == 0 ):
    print ("Monday")
if (weekday == 1 ):
    print ("Tuesday")
if (weekday == 2 ):
    print ("Wednesday")
if (weekday == 3 ):
    print ("Thursday")
if (weekday == 4 ):
    print ("Friday")
if (weekday == 5 ):
    print ("Saturday")
if (weekday == 6 ):
    print ("Sunday")
