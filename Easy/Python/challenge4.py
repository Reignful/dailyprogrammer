''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Author: Josh Vocal
Version 1.0
Description: Create a random password generator
Changes:
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#imports
import random
import string

#functions

#main
#Creates a variable that contains a set of letters, digits and punctucation
characters = string.letters + string.digits + string.punctuation
numChar = input("How many characters would you like in your password? ")
for letter in range(input("How many passwords would you like to create? ")):
    #Joins a string from the list in the variable 'characters' of length 'numChar'
    print "".join(random.sample(characters, numChar))

