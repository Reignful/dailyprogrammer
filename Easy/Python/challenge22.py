'''
Author: Josh Vocal
Description: Write a program that will compare two lists, and append any elements in the second list that dosen't exist in the first
Version 1.0
Changes:
'''

#Functions
def getList1():
    print ("Please enter elements into a list")
    lenList1 = input("How long do you want the list to be? ")
    list1 = []
    for i in range(lenList1):
       list1.append(raw_input("Please enter element %d: " %  i)) 
    return list1

def getList2():
    print ("Please enter elements into a list2")
    lenList2 = input("How long do you want the list ot be? ")
    list2 = []
    for j in range(lenList2):
        list2.append(raw_input("Please enter element %d: " % j))
    return list2

#Main
listSet = set(getList1() + getList2())
print ("The elements that don't appear the second list combined with the first list are:", listSet)
