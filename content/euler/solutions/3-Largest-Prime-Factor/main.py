from math import sqrt

def primes(n):
	primes = []
	sieve = [True] * (n + 1)
	for p in range(2, n + 1):
		if sieve[p]:
			primes.append(p)
			for i in range(p * p, n + 1, p):
				sieve[i] = False
	return primes

n = 600851475143
pmax = int(sqrt(n))
out = 2

for p in primes(pmax):
	if n % p == 0:
		out = p
print(out)