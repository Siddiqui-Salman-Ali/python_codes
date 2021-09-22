# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 00:27:00 2021

@author: EngrS
"""


FavouriteSongDict = {"NameOfSong":"I want in that way","NameofBand":"Backstreet Boys","GenreofSong":"Pop",
                     "LabelName":"Jive","NameofAlbum":"Millennium","ReleaseDate":"12-04-1999",
                     "SongDuration":"213","writers": "Andreas Carlsson & Max Martin"}



for members in FavouriteSongDict:
    print("\n The key is ",members ," and the corresponding value is", FavouriteSongDict[members])
    

print("\n..."*3)
    
#Here we take input from user to pass it as an argument to the function
    
key = input(str("Please guess a key name: "))
value = input(str("Please guess the value:  "))

#Declarinf Key and Values list as global variables

Key =[]
Values = []


def guessWhat(key,value):
    """ 
    The function takes in 2 arguments both in
    key: in string fromat
    value: in string format
    
    the fucntion then stores all the keys from dectionary to
    Key list and all the Values in Values list.
    We then compar the user input to the correct key and
    value pair where user is given 3 chance to predict the
    correct pair and returns True else returns False.
    """
    keyCounter = 3
    valueCouter = 3
    for members in FavouriteSongDict:
        Key.append(members)
        Values.append(FavouriteSongDict[members])   
    while (True):
        if key in Key:
            print("The key exists")
            print("...\n"*3)
            if FavouriteSongDict[key]==value:
                print("Congratulations you have guessed the correct key value pair")       
                return True
            else:
                print("x \t x \t x \t\n"*2)
                print ("Sorry you have {} attempts left, please type the correct value ".format(valueCouter),end="")
                value = input(str(" here: " ))
                valueCouter -=1
                if valueCouter > 0:
                    continue
                else:
                    print("x \t x \t x \t\n"*2)
                    print("Sorry you have no attempts left!")
                    return False
        else:
            print("x \t x \t x \t\n"*2)
            print ("Sorry you have {} attempts left, please type the correct key name ".format(keyCounter),end="")
            key = input(str("here: " ))
            keyCounter -=1
            if keyCounter > 0:
                continue
            else:
                print("Sorry you have no attempts left!")
                return False
        break
                
#calling function with user input as an argument
guessWhat(key,value)

                
    
