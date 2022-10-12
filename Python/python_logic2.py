#!/usr/bin/env python3
import sys
count = 50
if count < 0:
  print ('negative')
if count > 0:
  message = 'positive'
  print('the number is',message)
if count < 50:
  message = 'this number is smaller than 50'
  print(message)
  if count %2 == 0:
   message = 'Even number'
   print(message)
else:
  if count %2 == 0:
    print('Even number')
if count > 50:
  message = 'this number is larger than 50'
  print(message)
  if count %3 == 0:
   message = 'and divisible by 3'
   print(message)
if count %3 == 0:
   message = 'this number is divisible by 3'
   print(message)
if count == 50:
  message = 'The number is 50'
  print(message)
if count == 0:
  message = 'The number is zero'
  print(message)
