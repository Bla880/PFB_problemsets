#!/usr/bin/env python3

number = [101,2,15,22,95,33,2,27,72,15,52]
numbers = sorted(number)
even_l = []
odd_l = []

for number in numbers:
  if number %2 == 0:
    even_l.append(number)
  else:
    odd_l.append(number) 

cumulative=0
for number in even_l:
  cumulative = cumulative+number
print('Sum of even numbers',cumulative)

cumulative=0
for number in odd_l:
  cumulative = cumulative+number
print('Sum of odd numbers',cumulative)  
