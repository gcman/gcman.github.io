from math import sqrt

# Sieve of Eratosthenes
def primes(n):
	primes = []
	sieve = [True] * (n + 1)
	for p in range(2, n + 1):
		if sieve[p]:
			primes.append(p)
			for i in range(p * p, n + 1, p):
				sieve[i] = False
	return primes

# Use trial division to test if n is prime
def is_prime(n):
	# We don't want negative primes
	if n <= 0:
		return False
	return not any([n%i==0 for i in range(2,int(sqrt(n))+1)])

N = int(input())
P = primes(N)
# The maximal no. of primes generated so far
COUNT = 0
# The coefficients that generate COUNT primes
COEFF = []
for a in range(1,N+1,2):
	for b in P:
		# Iterate over +/- a,b
		for sgna in [-1,1]:
			for sgnb in [-1,1]:
				# No. of primes given by a,b
				count = 0
				# The quadratic given by a,b
				f = lambda x: x*x + sgna*a*x + sgnb*b
				# Keep going until f(x) is not prime
				while f(count) > 0 and is_prime(f(count)):
					count += 1
				# Only keep the maximum so far
				if count > COUNT:
					COUNT = count
					# Update coefficients
					COEFF = [sgna*a,sgnb*b]
print("{} {}".format(COEFF[0],COEFF[1]))