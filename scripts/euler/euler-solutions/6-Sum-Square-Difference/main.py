T = int(input())
for _ in range(T):
	N = int(input())
	ans = abs((3*N**4 + 2*N**3 - 3*N**2 - 2*N)//12)
	print(ans)