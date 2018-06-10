# Written by Gautam Manohar
# NOTE: WRONG
from collections import Counter
from math import factorial

def primes(n):
	primes = []
	sieve = [True] * (n + 1)
	for p in range(2, n + 1):
		if sieve[p]:
			primes.append(p)
			for i in range(p * p, n + 1, p):
				sieve[i] = False
	return primes

def fact_prime(LIM):
	P = primes(LIM)
	PF = []
	C = Counter()
	for n in range(LIM):
		for p in P:
			if p > n:
				break
			while n % p == 0:
				n //= p
				C[p] += 1
	return C

def binom_squarefree(n,k):
	COUNT = fact_prime(n) - fact_prime(k) - fact_prime(n-k)
	COUNT = COUNT.most_common(1)
	return not COUNT or COUNT[0][1] < 2, COUNT

def product(arr):
	out = 1
	for x in arr:
		out *= x
	return out

S = set([])
for n in range(51):
	for k in range(n+1):
		B = binom_squarefree(n,k)
		if B[0]:
			S.add(product([x[0] for x in B[1]]))
print(sum(S))