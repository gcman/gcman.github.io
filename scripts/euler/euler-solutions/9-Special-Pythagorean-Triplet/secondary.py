from math import sqrt

MAX = 3000
S = [-1]*3001
for a in range(1,MAX//2 - 1):
	for b in range(a+1,MAX-a):
		c = int(sqrt(a**2 + b**2))
		if c**2 == a**2 + b**2:
			perimeter = a + b + c
			if perimeter > MAX:
				break
			S[perimeter] = max(S[perimeter],a*b*c)

T = int(input())
for _ in range(T):
	N = int(input())
	print(S[N])