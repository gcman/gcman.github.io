N = int(input())
memo = [0] * (N + 1)
def min_pf(n):
	sieve = [0] * (n + 1)
	for p in range(2, n + 1):
		if sieve[p] == 0:
			memo[p] = p - 1
			for i in range(p, n + 1, p):
				sieve[i] = p
	return sieve

F = min_pf(N)
def phi(n):
	if memo[n] == 0:
		f = F[n]
		exp = 0
		ndiv = n
		while ndiv % f == 0:
			exp += 1
			ndiv //= f
		if ndiv == 1:
			memo[n] = f**(exp-1) * (f-1)
		else:
			memo[n] = memo[n//f**exp] * memo[f**exp]
	return memo[n]

def min_ratio(n):
	min_quot = (n,1)
	def is_perm(a,b):
		return sorted(str(a)) == sorted(str(b))
	for i in range(2,n):
		if is_perm(i,phi(i)):
			if i * min_quot[1] < min_quot[0] * phi(i):
				min_quot = (i,phi(i))
	return min_quot[0]

print(min_ratio(N))