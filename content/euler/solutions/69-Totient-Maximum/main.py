def primes(n):
	primes = []
	sieve = [True] * (n + 1)
	for p in range(2, n + 1):
		if sieve[p]:
			primes.append(p)
			for i in range(p * p, n + 1, p):
				sieve[i] = False
	return primes

P = primes(53)
def max_ratio(n):
	out = 1
	i = 0
	while out*P[i] < n:
		out *= P[i]
		i += 1
	return out

T = int(input())
for _ in range(T):
	N = int(input())
	print(max_ratio(N))