T = int(input())
for _ in range(T):
	N = int(input())
	ans = -1
	for a in range(1,N//3):
		b = (N**2 - 2*a*N)/(2*N - 2*a)
		c = N - a - b
		if b == int(b) and c == int(c) and c**2 == a**2 + b**2:
			ans = max(ans,int(a*b*c))
	print(ans)