ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def score(s):
	return sum([ALPH.index(x) for x in s]) + len(s)

N = int(input())
names = sorted([input().strip() for _ in range(N)])
Q = int(input())
for _ in range(Q):
	name = input().strip()
	ans = score(name)*(names.index(name) + 1)
	print(ans)