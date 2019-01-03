import sys
# We use this to speed up reading stdin
# Because we have a lot of names to read
input = sys.stdin.readline

# Reference alphabet
ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def score(s):
	# index starts at 0
	# So score is the sum of (index + 1) for each letter
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