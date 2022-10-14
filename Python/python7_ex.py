#!/usr/bin/env python3

import re

with open('Python_07_nobody.txt','r') as raw:
  i = 0
  for line in raw:
    i += 1
    found = len((re.findall(r'Nobody',line)))
    for position in re.finditer(r'Nobody',line):
      n_start = position.start()
      n_end  = position.end()
      print('In line',i,'# words:',found,'startin from',n_start,'to',n_end,sep='\t')
