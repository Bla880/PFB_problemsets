#!/usr/bin/env python3

###Problem8
num_lines = sum(1 for line in open('Python_06.fastq')) 
print('Number of lines in the file',num_lines)

file = open('Python_06.fastq','r') 
data = file.read()
number_charact = len(data)
print('Number of characters in the file',number_charact)
file.close()

with open('Python_06.fastq','r') as f:
  lines = f.readlines()
  print(sum(len(line) for line in lines) / len(lines))





