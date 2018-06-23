import sys
input = sys.stdin.readline

ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def score(s):
	# index starts at 0
	# So score is the sum of (idx + 1)
	return sum([ALPH.index(x) for x in s]) + len(s)

N = int(input())
names = sorted([input().strip() for _ in range(N)])
Q = int(input())
for _ in range(Q):
	# Remove any possible whitespace
	name = input().strip()
	# Index starts at 0
	ans = score(name)*(names.index(name) + 1)
	print(ans)