# Written by Gautam Manohar

def primes(n):
	primes = []
	sieve = [True] * (n + 1)
	for p in range(2, n + 1):
		if sieve[p]:
			primes.append(p)
			for i in range(p * p, n + 1, p):
				sieve[i] = False
	return primes

def binarySearch(arr,l,r,x):
	while l <= r:
		mid = l + (r-l)//2
		if arr[mid] == x:
			return mid
		elif arr[mid] < x:
			l = mid + 1
		else:
			r = mid - 1
	return r

N = int(1e8)
P = primes(N//2)
count = sum([max(0,binarySearch(P,i,len(P)-1,N//p)-i+1) for i,p in enumerate(P)])
print(count)