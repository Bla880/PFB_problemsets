#!/usr/bin/env python3
import sys
count = 10
if count > 0:
  message = 'positive'
  print('the number is',message)
elif count < 50:
  message = 'smaller than 50'
  print(message)
elif (count > 0) and (count < 50):
  message = 'smaller than 50'
  print('the number is positive and',message)
elif (count == 50) and (count < 50):
  message = 'smaller than 50'
  print('even and',message)
else:
  message = 'The number is zero'
  print(message)
