from math import sqrt
from itertools import combinations

def is_perm(n,m):
	return sorted(str(n)) == sorted(str(m))

def primes(n):
	primes = [1]
	sieve = [True] * (n+1)
	for p in range(2, n+1):
		if sieve[p]:
			primes.append(p)
			for i in range(p*p, n+1, p):
				sieve[i] = False
	return primes

N = int(input())
upper = int(sqrt(N) * 1.3)
lower = int(sqrt(N) * 0.7)
if N < 500**2:
	lower = 0
P = [p for p in primes(upper) if lower <= p]
P.append(1)
MIN = (N+1,N+1)

for comb in combinations(P,3):
	phi = 1
	n = 1
	for p in comb:
		if p != 1:
			phi *= (p-1)
		n *= p
	if n <= N:
		if is_perm(phi,n):
			print(n)
			phi = n/phi
			if phi < MIN[0]:
				MIN = (phi,n)
print(MIN[1])