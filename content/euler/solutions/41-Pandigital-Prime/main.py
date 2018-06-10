# Written by Gautam Manohar

N = 7654321

def primes(n):
	primes = []
	sieve = [True] * (n + 1)
	for p in range(2, n + 1):
		if sieve[p]:
			primes.append(p)
			for i in range(p * p, n + 1, p):
				sieve[i] = False
	return primes

candidates = [x for x in primes(N) if (int(1e3)-1 < x and x < int(1e4)) or (int(1e6)-1 < x < int(1e7))]
pandigital = []
for x in candidates:
	x = str(x)
	if all([str(d) in x for d in range(1,len(x)+1)]):
		pandigital.append(x)
print(max(pandigital))