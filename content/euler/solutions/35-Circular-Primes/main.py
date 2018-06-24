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

# Get all the rotated versions of integer x
def rotations(x):
	x = str(x)
	out = []
	for i in range(len(x)):
		# Move last char in x to front
		x = x[-1] + x[:-1]
		out.append(int(x))
	return out

N = int(input())
P = primes(int(1e6))
CIRCULAR = set()
# Make sure we don't exceed upper bound
for x in [p for p in P if p < N]:
	# Exclude primes with even digits or 5; they can't be circular
	# Except when x = 2 or x = 5; include those, because they are circular
	if len(str(x)) == 1 or not set([d for d in "024568"]) & set([d for d in str(x)]):
		# Avoid duplicates
		if x not in CIRCULAR:
			ROT = rotations(x)
			# Make sure all of the rotations are prime
			if all([rot in P for rot in ROT]):
				for rot in ROT:
					# Add the rotations that are less than N
					if rot < N:
						CIRCULAR.add(rot)
print(sum(CIRCULAR))