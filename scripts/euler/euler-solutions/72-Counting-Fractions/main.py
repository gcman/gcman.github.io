MAX = int(1e6)
memo = [0] * (MAX + 1)

# Sieve of Eratosthenes
# Return totient of i for all i < n
def phi(n):
	PHI = [0] * (n+1)
	for p in range(2, n + 1):
		# If p is prime, set its totient value
		# and that of all its multiples
		if PHI[p] == 0:
			PHI[p] = p-1
			for i in range(2*p, n + 1, p):
				# Initialize phi(i)
				if PHI[i] == 0:
					PHI[i] = i
				# Use Euler product formula
				PHI[i] -= PHI[i]//p
	return PHI

# Create prefix sum array
S = []
count = 0
for n in phi(MAX):
	count += n
	S.append(count)

T = int(input())
for _ in range(T):
	N = int(input())
	print(S[N])