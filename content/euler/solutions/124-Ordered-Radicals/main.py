# Written by Gautam Manohar

def primes(n):
	primes = []
	sieve = [True] * (n + 1)
	for p in range(2, n + 1):
		if sieve[p]:
			primes.append(p)
			for i in range(p * p, n + 1, p):
				sieve[i] = False
	return primes

P = primes(316)
RAD = []
for n in range(int(1e5)):
	norig = n + 1
	n += 1
	for p in P:
		while n % p == 0 and (n//p) % p == 0:
			n //= p
	RAD.append((norig,n))

RAD = sorted(RAD,key=lambda x: x[1])
print(RAD[9999][0])