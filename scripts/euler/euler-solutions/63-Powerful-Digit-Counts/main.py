from math import ceil
N = int(input())
lo = ceil(10**(1 - 1/N))
for n in range(lo,10):
	print(n**N)