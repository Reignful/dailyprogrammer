''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Author: Josh Vocal
Version 1.0
Description: Creates a ceaser cipher on the user's input message
Changes:
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#Functions
def mode():
    while True:
        mode = raw_input("Do you want to encrypt or decrypt a message? ").lower()
        #Checks if the user's input is in the list ['encrypt', 'decrpyt']
        if mode in 'encrypt decrypt'.split():
            return mode
        else:
            print("Enter either 'encrypt or decrypt'")
#Main
mode();
