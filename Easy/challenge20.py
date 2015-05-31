#Finds all prime numbers between 2 integers and returns them.
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
