#!/usr/bin/env python3
import sys 
import re
file_f = sys.argv[1]
seqs = {}
count_nt = {}
dict_count= {}

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

dictionary_counts ={}
for it in seqs:
  seq = seqs[it]
  dictionary_counts[it]={'nt_comp':{},'seq':seq}
  unique=set(seq)
  for nt in unique:
    dictionary_counts[it]['nt_comp'][nt]=seq.count(nt)

print(dictionary_counts)


