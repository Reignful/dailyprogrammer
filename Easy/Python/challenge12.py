'''
Author: Josh Vocal
Description: A program that prints all the possible permutations of the string
Version 1.0
Changes:
'''

#Import
import itertools

#Main
counter = 0
userinput = raw_input("Please input and the program will print all possible permutations ")
permalist = list(itertools.permutations(userinput))
for x in permalist:
    print ("".join(x))
    counter += 1
print ("%d elements") % (counter)
