#!/usr/bin/env python3
import sys
count = sys.argv[1]

if count < 0:
  message = ' is negative'
  print (count,message)
if count > 0:
  message = ' is positive'
  print(count,message)
if count < 50:
  message = ' is smaller than 50'
  print(count,message)
  if count %2 == 0:
   message = ' is an even number'
   print(count,message)
else:
  if count %2 == 0:
   message = ' is an even number'
   print(count,message)
if count > 50:
  message = '  is larger than 50'
  print(count,message)
  if count %3 == 0:
   message = ' is divisible by 3'
   print(count,message)
if count %3 == 0:
   message = ' is divisible by 3'
   print(count,message)
if count == 50:
  message = ' is 50'
  print(count,message)
if count == 0:
  message = ' is zero'
  print(count,message)
