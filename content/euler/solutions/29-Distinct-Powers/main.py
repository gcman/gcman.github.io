from math import log

def prod(arr):
	out = 1
	for x in arr:
		out *= x
	return out

def gcd(a,b):
	while b:
		a, b = b, a%b
	return a

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
	P = primes(n)
	sieve = {}
	for p in P:
		for exp in range(1,int(log(n,p))+1):
			for i in range(p**exp,n+1,p**exp):
				if i not in sieve:
					sieve[i] = {}
				if p not in sieve[i]:
					sieve[i][p] = 0
				sieve[i][p] += 1
	return sieve

N = int(input())
FACTORS = prime_factors(N)
def cartesian(arrs):
    if not arrs:
    	return [()]
    return [x + (y,) for x in cartesian(arrs[:-1]) for y in arrs[-1]]

def factors(n):
	if n == 1:
		return set([1])
	F = FACTORS[n]
	prime_factorizations = cartesian([list(range(F[p]+1)) for p in F])
	out = set()
	for x in prime_factorizations:
		prime_powers = []
		for i,exp in enumerate(x):
			prime_powers.append(sorted(list(F.keys()))[i]**exp)
		out.add(prod(prime_powers))
	return out

def distinct(a,n):
	F = FACTORS[a]
	pf = sorted(F.keys())
	exponents = [F[p] for p in pf]
	GCD = exponents[0]
	for e in exponents:
		GCD = gcd(GCD,e)
	count = 0
	for f in factors(GCD):
		if f != 1:
			count += n//f - 1
	return n - 1 - count

for i in range(2,N+1):
	print(i,len(set([a**b for a in range(2,i+1) for b in range(2,i+1)])))