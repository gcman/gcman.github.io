# Written by Gautam Manohar
# Key observation: a circular prime of more than one digit must not contain even digits or 5

def primes(n):
	primes = set([])
	sieve = [True] * (n + 1)
	for p in range(2, n + 1):
		if sieve[p]:
			primes.add(p)
			for i in range(p * p, n + 1, p):
				sieve[i] = False
	return primes

N = int(1e6)
P = primes(N)

def circles(n):
	n = str(n)
	return set([int(n[i:] + n[:i]) for i in range(len(n))])

def is_circular(n):
	if x > 9:
		if any(digit in [0,2,4,5,6,8] for digit in [int(d) for d in str(n)]):
			return False
	return all(x in P for x in circles(n))

circular = set([])
for x in P:
	if x not in circular:
		if is_circular(x):
			for p in circles(x):
				circular.add(p)
print(len(circular))