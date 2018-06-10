# Written by Gautam Manohar
# NOTE: BRUTE FORCE SOLUTION, DOES NOT CURRENTLY WORK
from collections import Counter

def primes(n):
	primes = []
	sieve = [True] * (n + 1)
	for p in range(2, n + 1):
		if sieve[p]:
			primes.append(p)
			for i in range(p * p, n + 1, p):
				sieve[i] = False
	return primes

N = 3163
P = primes(N)

def phi(n):
	out = n
	for p in P:
		if n % p == 0:
			out *= (1 - 1/p)
			while n % p == 0:
				n //= p
	if n != 1:
		out *= (1 - 1/n)

PERM = []

for n in range(1,int(1e7)+1):
	PHI = phi(n)
	print(n)
	if Counter(str(n)) == Counter(str(PHI)):
		PERM.append((n,n/PHI))
		print(PERM)

PERM = sorted(PERM,key=lambda x: x[1])
print(PERM[0][0])