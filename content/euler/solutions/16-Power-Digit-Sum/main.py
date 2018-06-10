# Written by Gautam Manohar
N = 2**1000
S = 0
while N >= 1:
	S += N % 10
	N -= N % 10
	N //= 10
	print(N)
print(S)