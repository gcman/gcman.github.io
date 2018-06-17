def perms(s):        
	if len(s) == 1:
		return [s]
	out = []
	for i,v in enumerate(s):
		out += [v+p for p in perms(s[:i]+s[i+1:])]
	return out

def primes(n):
	primes = []
	sieve = [True] * (n + 1)
	for p in range(2, n + 1):
		if sieve[p]:
			primes.append(p)
			for i in range(p * p, n + 1, p):
				sieve[i] = False
	return primes

def pandigital():
	root = "123456789"
	out = []
	for i in [4,7]:
		out += perms(root[:i])
	return [int(x) for x in out]

def bs(arr, l, r, x):
	while l <= r:
		mid = l + (r - l)//2;
		if arr[mid] == x:
			return arr[mid]
		elif arr[mid] < x:
			l = mid + 1
		else:
			r = mid - 1
	if r == -1:
		return r
	return arr[r]

P = primes(int(31426))
PAN = pandigital()
PAN_PRIME = []
for pan in PAN:
	if pan in P or not any([pan%p == 0 for p in P if p <= int(pan**0.5)]):
		PAN_PRIME.append(pan)

T = int(input())
for _ in range(T):
	N = int(input())
	print(bs(PAN_PRIME,0,len(PAN_PRIME)-1,N))