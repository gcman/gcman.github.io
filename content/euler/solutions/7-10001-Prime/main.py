from math import log

def primes(n):
	primes = []
	sieve = [True] * (n + 1)
	for p in range(2, n + 1):
		if sieve[p]:
			primes.append(p)
			for i in range(p * p, n + 1, p):
				sieve[i] = False
	return primes

def n_primes(n):
	upper = int(n*log(n) + n*log(log(n)))
	return primes(upper)

T = int(input())
P = n_primes(10000)
for _ in range(T):
	N = int(input())
	print(P[N-1])