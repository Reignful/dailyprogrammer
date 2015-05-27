'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Author: Josh Vocal
Version 1.0
Description: A program that will print the song "99 bottles of beer on the wall"
Changes:
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#Main
for beer in range(99, -1, -1):
    if (beer == 0):
        print ("%d bottles of beer on the walll %d bottles of beer! No more bottles of beer on the wall!") % (beer, beer)
    elif (beer >= 2 or beer < 1):
        print ("%d bottles of beer on the wall %d bottles of beer! Take one down, pass it around, %d bottles of beer on the wall!") % (beer, beer, beer)
    elif (beer == 1):
        print("%d bottle of beer on the wall %d bottle of beer! Take one down, pass it around, %d bottle of beer on the wall!") % (beer, beer, beer)
