# Written by Gautam Manohar

N = 10000

def primes(n):
	primes = []
	sieve = [True] * (n + 1)
	for p in range(2, n + 1):
		if sieve[p]:
			primes.append(p)
			for i in range(p * p, n + 1, p):
				sieve[i] = False
	return primes

def permutations(n):
	n = str(n)
	if "0" in n:
		return [int(n)]
	perms = []
	a = list(range(len(n)))
	switches = [(x,y) for x in a for y in a if x != y]
	for x in switches:
		switches.remove((x[1],x[0]))
	for x in switches:
		n_new = [None]*len(n)
		for i,y in enumerate(n):
			if i == x[0]:
				n_new[i] = n[x[1]]
			elif i == x[1]:
				n_new[x[1]] = n[x[0]]
			else:
				n_new[i] = n[i]
		perms.append(n_new)
	perms = [int("".join(x)) for x in perms]
	return perms
P = [x for x in primes(N) if x > 999]
for p in P:
	ttab = [x in P for x in permutations(p)]
	if sum(ttab) == 3:
		S = sorted([permutations(p)[i] for i,x in enumerate(ttab) if x == True])
		print(S, [S[2] - S[1], S[1] - S[0]])