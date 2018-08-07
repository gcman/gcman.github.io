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

# Binary search
def bs(arr, l, r, x):
	while l <= r:
		mid = l + (r - l)//2;
		if arr[mid] == x:
			return mid + 1
		elif arr[mid] < x:
			l = mid + 1
		else:
			r = mid - 1
	return r + 1

MAX = int(5e7)
P = primes(int(MAX**(1./2.)))
p2 = [p**2 for p in P]
p3 = [p**3 for p in P if p < MAX**(1./3.)]
p4 = [p**4 for p in P if p < MAX**(1./4.)]

sums = set()
for a in p2:
	for b in p3:
		for c in p4:
			sums.add(a+b+c)
sums = list(sorted(sums))

T = int(input())
for _ in range(T):
	N = int(input())
	print(bs(sums,0,len(sums)-1,N))