'''
Author: Josh Vocal
Description: Create a program that finds prime numbers
Version 1.0
Changes:
'''
#Main
lower = input("Enter lower range: ")
upper = input("Enter upper range: ")

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print (num)
