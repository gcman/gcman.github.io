import math

def primes(n):
	primes = []
	sieve = [True] * (n + 1)
	for p in range(2, n + 1):
		if sieve[p]:
			primes.append(p)
			for i in range(p * p, n + 1, p):
				sieve[i] = False
	return primes

def prod(a):
    out = 1
    for i in a:
        out *= i
    return out

def min_mult(n):
    return prod([p**math.floor(math.log(n,p)) for p in primes(n)])
print(min_mult(20))