#!/usr/bin/env python3
import sys 
import re
file_f = sys.argv[1]
seqs = {}
with open(file_f,'r') as raw:
  for line in raw:
    line = line.strip()
    if '>' in line:
      genes_id = line
      seqs[genes_id]=""
    else:
      seq = line
      seqs[genes_id] += seq  
print(seqs)

