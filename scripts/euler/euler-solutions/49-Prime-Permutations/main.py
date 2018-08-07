def primes(n):
	primes = []
	sieve = [True] * (n + 1)
	for p in range(2, n + 1):
		if sieve[p]:
			primes.append(p)
			for i in range(p * p, n + 1, p):
				sieve[i] = False
	return primes

def perms(s):       
	if len(s) == 1:
		return [s]
	out = []
	for i,u in enumerate(s):
		out += [u+v for v in perms(s[:i]+s[i+1:])]
	return out

N,K = map(int,input().split())
P = primes(10**len(str(N-1)))
def prime_perms(p,k):
	out = sorted([int(x) for x in perms(str(p)) if int(x) in P])
	if len(out) >= K:
		return out
	return []

out = set()
for p in P:
	PERMS = prime_perms(p,K)
	if PERMS:
		for i,p1 in enumerate(PERMS):
			if p1 < N:
				for j,p2 in enumerate(PERMS):
					if p2 > p1 and 2*p2 - p1 in PERMS:
						S = str(p1)+str(p2)+str(2*p2-p1)
						if len(S) == 3*len(str(p1)):
							out.add(S)
for x in sorted(out):
	print(x)