'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Author: Josh Vocal
Description: Write a program that will allow the user to input digits, and arrange them in numerical order.
Version 1.0
Changes:
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#Main
userinput = raw_input("Whatever you input here will be sorted ")
# Sorted(userinput) creates a list and "".join creates the list into a string.
print "".join(sorted(userinput))
