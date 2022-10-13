#!/usr/bin/env python3

seqs = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
seqs_it = iter(seqs)
for seq in seqs_it: 
  print(len(seq),'\t',seq)

 
