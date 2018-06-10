def bs(arr, l, r, x):
	while l <= r:
		mid = l + (r - l)//2;
		if arr[mid] == x:
			return mid
		elif arr[mid] < x:
			l = mid + 1
		else:
			r = mid - 1
	return r

def primes(n):
	primes = []
	sieve = [True] * (n + 1)
	for p in range(2, n + 1):
		if sieve[p]:
			primes.append(p)
			for i in range(p * p, n + 1, p):
				sieve[i] = False
	return primes

PRIMES = primes(int(1e6))
P = [0]
count = 0
for p in PRIMES:
	count += p
	P.append(count)

T = int(input())
for _ in range(T):
	N = int(input())
	idx = bs(PRIMES,0,len(PRIMES)-1,N)
	print(P[idx+1])