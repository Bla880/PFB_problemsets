#!/usr/bin/env python3
import sys 
import re
file_f = sys.argv[1]
seqs = {}
count_nt = {}
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

dict_seq = seqs.values()
dict_seq_list = list(dict_seq)
for seq in dict_seq_list:
  for nt in seq:
    count = seq.count(nt)
    count_nt[nt] = count
  print('nt_count',count_nt)
total_A = count_nt['A']
total_C = count_nt['C']
total_G = count_nt['G']
total_T = count_nt['T']
lenght_seq2 = len(seq)
GC_count = total_C + total_G
GC_content = (GC_count/lenght_seq2)*100
print(f'the GC content of this sequence is {GC_content:.2f}%')  

for line in count_nt:      
  
