#!/usr/bin/env python3
import sys
family = ['Luis','Miguel','Brianda','Alicia']
my_name = sys.argv[1]

if my_name in family:
  message = 'is member of Avina family'
  print('True',my_name,message) 
else:
  message2 = 'is NOT a member of Avina family'
  print('False',my_name,message2)
