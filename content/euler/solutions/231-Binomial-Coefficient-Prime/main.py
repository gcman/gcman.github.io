# Written by Gautam Manohar
# NOTE: WRONG
from collections import Counter
from math import log,floor

def primes(n):
	primes = []
	sieve = [True] * (n + 1)
	for p in range(2, n + 1):
		if sieve[p]:
			primes.append(p)
			for i in range(p * p, n + 1, p):
				sieve[i] = False
	return primes

def fact_prime(n):
	P = primes(n)
	C = Counter()
	for p in P:
		C[p] = sum([n//p**k for k in range(1,floor(log(n,p)))])
	return C

def prime_sum(COUNT):
	return sum([x[0]*x[1] for x in COUNT.items()])

def bin_prime_sum(n,k):
	return prime_sum(fact_prime(n) - fact_prime(k) - fact_prime(n-k))

print(bin_prime_sum(20000000,15000000))