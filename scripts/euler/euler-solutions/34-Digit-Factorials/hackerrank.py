from math import factorial

def dig_fact(n):
	return sum([factorial(int(x)) for x in str(n)])

N = int(input())
print(sum([x for x in range(10,N+1) if dig_fact(x) % x == 0]))