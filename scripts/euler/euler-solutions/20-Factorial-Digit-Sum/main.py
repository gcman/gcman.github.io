from math import factorial

def digit_sum(n):
	return sum([int(x) for x in str(n)])

T = int(input())
for _ in range(T):
	N = int(input())
	print(digit_sum(factorial(N)))