'''
Author: Josh Vocal
Version 1.0
Changes:
Description: A calculator that calculates mass, force or acceleration.
'''

#Imports
import math

#Functions
def intro():
    print("Hello, this is a simple program that calculates mass, force or acceleration.")

def calcf():
    m = input("What is the mass in kg? ")
    a = input("What is the acceleration in m/s? ")
    f = m*a
    print ("The force is %s newtons") % (f)
    return

def calca():
    f = input("What is the force in newtons? ")
    m = input("What is the mass in kg? ")
    a = f/m
    print ("The acceleration is %s m/s") % (a)
    return

def calcm():
    f = input("What is the force in newtons? ")
    a = input("What is the acceleration in m/s? ")
    m = f/a
    print ("The mass is %s kg") % (m)
    return

def endmsg():
    print "Goodbye, have a nice day!"

#Main
intro();
choice = "y"
while (choice == "y"):
    selection = raw_input("What would you like to calculate? \n m = mass\n f = force\n a = acceleration\n")
    while (selection != 'f' and selection != 'm' and selection != 'a'):
        selection = raw_input("Please select\n m = mass\n f = force\n a = acceleration\n")
    if (selection == 'f'):
        calcf();
    if (selection == 'm'):
        calcm();
    if (selection == 'a'):
        calca();
    choice = raw_input("Do you want to do another calculation? \ny = yes\n")
endmsg();
