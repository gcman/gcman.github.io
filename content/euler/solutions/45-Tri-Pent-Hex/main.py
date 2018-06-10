# Written by Gautam Manohar
import math

def isPent(n):
	test = (1+math.sqrt(24*n + 1))/6
	return test == int(test)

def findNext(n):
	while True:
		n += 1
		res = n*(2*n - 1)
		if isPent(res):
			return res
print(findNext(143))