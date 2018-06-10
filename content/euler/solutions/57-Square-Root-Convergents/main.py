# Written by Gautam Manohar
import math

def next_convergent(p,q):
	return p+2*q,p+q

S = []
p,q = 1,1
for _ in range(1000):
	p,q = next_convergent(p,q)
	if math.floor(math.log(p,10)) > math.floor(math.log(q,10)):
		S.append((p,q))
print(len(S))