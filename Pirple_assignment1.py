# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 00:27:00 2021

@author: EngrS
"""
"""
The assignment focuses on declaring attributes of
my favorite songs and printing all the variable with
suitable concatenation method.
"""

#Declaring the name of song type string.

NameOfSong = "I want in that way"

#Declaring the name of band type string.

NameofBand = "Backstreet Boys"

#Declaring the genre of the song, type string

GenreofSong = "Pop"

#Label of the record company

LabelCall = "Jive"


#Declaring the name of album , type = string

NameofAlbum = "Millennium"

#Declaring the Releasedate of the song 

ReleaseDate = "12-04-1999"

#Duration of the song in seconds , type = integer

SongDuration = 213

#Song lyricists , type = string

writer1 , writer2 = "Andreas Carlsson" , "Max Martin"

#print function will concatinate and print all the values 
print ("My favoirite song is "+"\""+NameOfSong+"\" and is sung by my \""+NameofBand +
       "\" .This is a "+ GenreofSong + " song which was was released on " +ReleaseDate + " and is the the most popular song of the album " + NameofAlbum+
       ". The {} seconds long song is full of ups and downs ".format(SongDuration))

