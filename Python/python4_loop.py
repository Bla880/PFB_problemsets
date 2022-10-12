#!/usr/bin/env python3

taxa = 'sapiens,erectus,neardenthal'
print(taxa)
print(taxa[1])

specie = taxa.split(',')
print(specie)

###sorting 
sor_alpha=sorted(specie)
print(sor_alpha)
sor_len=sorted(specie,key=len)
print(sor_len)
