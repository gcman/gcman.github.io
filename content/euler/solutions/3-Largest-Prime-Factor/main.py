def primes(n):
	primes = []
	sieve = [True] * (n + 1)
	for p in range(2, n + 1):
		if sieve[p]:
			primes.append(p)
			for i in range(p * p, n + 1, p):
				sieve[i] = False
	return primes

def prime_factors(n):
	factors = []
	P = primes(int(n**0.5))
	for p in P:
		if n % p == 0:
			factors.append(p)
			while n % p == 0:
				n //= p
	if n != 1:
		factors.append(n)
	return factors

T = int(input())
for _ in range(T):
	N = int(input())
	ans = max(prime_factors(N))
	print(ans)