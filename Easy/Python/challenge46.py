'''
Author: Josh Vocal
Description: Convert a decimal number to binary and sum the bianry number.
'''

#Main
#Converts the input number into a binary number and slices it
#Joins "+" into the binary number. Ex "1+0+1+1"
#Uses the evaluation function to add the numbers in the string.
print(eval("+".join(bin(input("Please enter a number: "))[2:])))
