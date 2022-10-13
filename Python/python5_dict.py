#!/usr/bin/env python3

my_fav = {'book': 'Big Expectations','song':'This must be the place', 'flower': 'Rose'}
print(my_fav['book'])
fav_book = 'book'
print(my_fav[fav_book])

print(my_fav['flower'0])

my_fav['organism']='Axolotl'  #Add  new 'key' to the dictionary
fav_animal='organism'        #set organism to a variable 
print(my_fav[fav_animal])

my_fav['organism']='horse' #set key another value
print(my_fav)
fav_animal = 'organism'
print(my_fav[fav_animal])

####For loop to print our each key and value 
for fav in my_fav:
  description = my_fav[fav]
  print(fav,description[0:])


