# Written by Gautam Manohar
import math

def tetr(a,b,m):
	aorig = a
	for _ in range(b-1):
		a = pow(aorig,a,m)
	return a

print(tetr(1777,1855,int(1e8)))