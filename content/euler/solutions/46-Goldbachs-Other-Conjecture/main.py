def primes(n):
	primes = []
	sieve = [True] * (n + 1)
	for p in range(2, n + 1):
		if sieve[p]:
			primes.append(p)
			for i in range(p * p, n + 1, p):
				sieve[i] = False
	return primes

P = primes(int(5e5))
def ways(n):
	cand = lambda p: ((n-p)/2)**0.5
	return len(set(p for p in P if p < n and cand(p) == int(cand(p))))

T = int(input())
for _ in range(T):
	N = int(input())
	print(ways(N))