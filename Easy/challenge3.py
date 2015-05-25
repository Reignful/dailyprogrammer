''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Author: Josh Vocal
Version 1.0
Description: Creates a ceaser cipher on the user's input message
Changes:
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#Functions
max_key_size = 26

def mode():
    while True:
        mode = raw_input("Do you want to encrypt or decrypt a message? ").lower()
        #Checks if the user's input is in the list ['encrypt', 'decrpyt']
        if mode in 'encrypt decrypt'.split():
            return mode
        else:
            print("Enter either 'encrypt or decrypt'")

def msg():
    return raw_input("Enter your message that you want to encrypt: ")
    
def key():
    while True:
        print("Enter the key number (1 - %s)" % (max_key_size))
        key = int(input())
        #Checks if the key is within the alphabetical letter range shift
        if (key >= 1 and key <= max_key_size):
            return key

def translate(mode, msg, key):
    #Checks if we are encrytion or decrytion mode and translates the user's input
    if mode[0] == 'd':
        #In decryption mode, instead of adding the key, it subtracts the key
        key = -key
    translated = ""
    for symbol in msg:
    #Checks if the character is a alphabetical letter and translates it
        if symbol.isalpha():
            #Shifts the letter by the value of the key
            num = ord(symbol)
            num += key

            if symbol.isupper():
            #If key is 26, it will return the same letter unchanged
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.lower():
            #If key is 26, it will return the same letter unchaged
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
        #Appends the translated character into the variable tranlated
            translated += chr(num)
        else:
            translated += symbol
    return translated

#Main
mode = mode();
msg = msg();
key = key();
print("Your translated message is: ")
print(translate(mode, msg, key))
