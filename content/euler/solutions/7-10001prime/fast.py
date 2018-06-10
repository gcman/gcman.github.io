# Written by Gautam Manohar
from math import log

N = 10001

def primes(n):
	primes = []
	sieve = [True] * (n + 1)
	for p in range(2, n + 1):
		if sieve[p]:
			primes.append(p)
			for i in range(p * p, n + 1, p):
				sieve[i] = False
	return primes

def nth_prime(n):
	p_max = int(n*(log(n) + log(log(n))))
	return(primes(p_max)[n-1])

print(nth_prime(10001))