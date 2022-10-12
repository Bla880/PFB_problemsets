#!/usr/bin/env python3
import sys
count = sys.argv[1]

if int(count) < 0:
  message = ' is negative'
  print (count,message)
if int(count) > 0:
  message = ' is positive'
  print(count,message)
if int(count) < 50:
  message = ' is smaller than 50'
  print(count,message)
  if int(count) %2 == 0:
   message = ' is an even number'
   print(count,message)
else:
  if int(count) %2 == 0:
   message = ' is an even number'
   print(count,message)
if int(count) > 50:
  message = '  is larger than 50'
  print(count,message)
  if int(count) %3 == 0:
   message = ' is divisible by 3'
   print(count,message)
if int(count) %3 == 0:
   message = ' is divisible by 3'
   print(count,message)
if int(count) == 50:
  message = ' is 50'
  print(count,message)
if int(count) == 0:
  message = ' is zero'
  print(count,message)
