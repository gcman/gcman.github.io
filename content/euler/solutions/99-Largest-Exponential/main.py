# Written by Gautam Manohar
from math import log

S = []
with open("base_exp.txt","r") as f:
	for line in f:
		b,e = map(int,line.split(","))
		S.append(e*log(b))
print(S.index(max(S))+1)