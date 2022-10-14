#!/usr/bin/env python3

###Problem7
fa_dict={}
with open('Python_06.seq.txt','r') as seq_read, open('Python_06.seqFASTA.txt','w') as seq_write:
  for line in seq_read:
    line.rstrip
    line_list = line.split('\t') 
    fa_dict[line_list[0]] = line_list[1]
  for k , v in fa_dict.items():
    final_text = '>' + k + '\n' + v
    seq_write.write(final_text) 





