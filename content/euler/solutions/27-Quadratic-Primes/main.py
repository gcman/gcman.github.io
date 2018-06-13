def primes(n):
	primes = []
	sieve = [True] * (n + 1)
	for p in range(2, n + 1):
		if sieve[p]:
			primes.append(p)
			for i in range(p * p, n + 1, p):
				sieve[i] = False
	return primes

def is_prime(n):
	return not any([n%i==0 for i in range(2,int(n**0.5)+1)])

N = int(input())
P = primes(N)
COUNT = 0
COEFF = []
for a in range(1,N+1,2):
	for b in P:
		for sgna in [-1,1]:
			for sgnb in [-1,1]:
				count = 0
				f = lambda x: x*x + sgna*a*x + sgnb*b
				while f(count) > 0 and is_prime(f(count)):
					count += 1
				if count > COUNT:
					COUNT = count
					COEFF = [sgna*a,sgnb*b]
print("{} {}".format(COEFF[0],COEFF[1]))