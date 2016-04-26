'''
Author: Josh Vocal
Description: Write a function that takes two strings and removes 
from the first string any character that appears in the second string.
Version 1.0
Changes:
'''

#Functions
def getString1():
    string1 = list((raw_input("What is your name? ")))
    return string1 

def getString2():
    string2 = list((raw_input("What letters do you want to remove in the first string? ")))
    return string2

def removeLetter(string1, string2):
    #Checks if there is a common element between both lists and removes it.
    #Joins the first list to combine the elements into a string.
    for letter in string1[:]:
        if letter in string2:
            string1.remove(letter)
    print "".join(string1)
    
    
#Main
removeLetter(getString1(), getString2());
