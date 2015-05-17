'''
Author: Josh Vocal
Version: 1.0
Description: A simple program that asks the user name, age and username.
'''
#Imports

#Functions
def namecheck():
    global name
    name = raw_input("What is your first name? ")
    while name.isalpha() == False or len(name) > 10:
        if name.isalpha() == False:
            print ("Please enter alphabetical letters only")
        elif len(name) > 20:
            print ("Sorry, your name is too long.  Please enter your nickname.")
        name = raw_input("What is your first name? ")
    return name

def agecheck(): 
    global age
    age = raw_input("How old are you? ")
    while len(age) > 2 or age.isdigit() == False:
        if age.isdigit() == False:
            print ("Please enter digits only")
        elif len(age) > 2:
            print ("Please enter a realistic age")
        age = raw_input("How old are you? ")
    return age

def usernamecheck():
    global username
    username = raw_input("What is your username? ")
    while len(username) > 15:
        print ("Sorry, your username is too long")
        username = raw_input("What is your username? ")
    return age

def printmsg(name, age, username):
    print ("\nYour name is %s, you are %s years old and your username is %s.") % (name, age, username)

#Main Program
namecheck();
agecheck();
usernamecheck();
printmsg(name, age, username);
