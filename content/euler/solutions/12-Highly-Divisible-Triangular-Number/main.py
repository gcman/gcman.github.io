from math import sqrt,log

def primes(n):
	primes = []
	sieve = [True] * (n + 1)
	for p in range(2, n + 1):
		if sieve[p]:
			primes.append(p)
			for i in range(p * p, n + 1, p):
				sieve[i] = False
	return primes
def triangular(n):
	return (n*(n+1)/2)
def pmax(n):
	return int(n*(log(n) + log(log(n))))
def pfs(n):
	factors = {}
	for p in primes(pmax(n)):
		while n%p == 0:
			if p not in factors:
				factors[p] = 0
			factors[p] += 1
			n /= p 
	return factors


def divisors(n):
	f = pfs(n)
	out = 1
	for p in f:
		out *= f[p] + 1
	return out
print(pfs(101), divisors(101))
#def min_divs(n):
	#out = 1
	#ordered = sorted([pfs(n)[p] for p in pfs(n)], reverse = True)
	#x = len(ordered) + 6
	#print(x,pfs(n),[pfs(n)[p] for p in pfs(n)],ordered, primes(pmax(n)))
	#for i,p in enumerate(pfs(n)):
		#out *= primes(pmax(n))[i]**(p-1)
	#return(out)
count = 2
#while True:
	#print(count, divisors(triangular(count)))
	#if divisors(triangular(count))== 500:
		#break
	#count+=1
