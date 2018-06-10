# Written by Gautam Manohar
import math

def conv_coeff(n):
	if n == 0:
		return 2
	elif n % 3 == 2:
		return 2*(n+1)//3
	return 1

CONV = [(1,0),(conv_coeff(0),1)]
for i in range(2,102):
	A = conv_coeff(i-1)*CONV[i-1][0] + CONV[i-2][0]
	B = conv_coeff(i-1)*CONV[i-1][1] + CONV[i-2][1]
	CONV.append((A,B))

print(sum([int(x) for x in str(CONV[100][0])]))