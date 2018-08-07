from math import log

# Sieve of Eratosthenes
def primes(n):
	primes = []
	sieve = [True] * (n + 1)
	for p in range(2, n + 1):
		if sieve[p]:
			primes.append(p)
			for i in range(p * p, n + 1, p):
				sieve[i] = False
	return primes

# Implement eq. (1)
def min_mult(n):
	P = primes(n)
	ans = 1
	for p in P:
		ans *= p**int(log(n,p))
	return ans

T = int(input())
for _ in range(T):
	N = int(input())
	print(min_mult(N))