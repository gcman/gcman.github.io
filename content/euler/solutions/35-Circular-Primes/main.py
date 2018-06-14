def primes(n):
	primes = []
	sieve = [True] * (n + 1)
	for p in range(2, n + 1):
		if sieve[p]:
			primes.append(p)
			for i in range(p * p, n + 1, p):
				sieve[i] = False
	return primes

def rotations(x):
	x = str(x)
	out = []
	for i in range(len(x)):
		x = x[-1] + x[:-1]
		out.append(int(x))
	return out

N = int(input())
P = primes(int(1e6))
CIRCULAR = set()
for x in [p for p in P if p < N]:
	if len(str(x)) == 1 or not set([d for d in "024568"]) & set([d for d in str(x)]):
		if x not in CIRCULAR:
			ROT = rotations(x)
			if all([rot in P for rot in ROT]):
				for rot in ROT:
					if rot < N:
						CIRCULAR.add(rot)
print(sum(CIRCULAR))