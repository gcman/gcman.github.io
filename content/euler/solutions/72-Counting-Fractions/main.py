MAX = int(1e6)
memo = [0] * (MAX + 1)
def min_pf(n):
	sieve = [0] * (n + 1)
	for p in range(2, n + 1):
		if sieve[p] == 0:
			memo[p] = p - 1
			for i in range(p, n + 1, p):
				sieve[i] = p
	return sieve

F = min_pf(MAX)
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

S = [0,0]
count = 0
for n in range(2,MAX+1):
	count += phi(n)
	S.append(count)

T = int(input())
for _ in range(T):
	N = int(input())
	print(S[N])