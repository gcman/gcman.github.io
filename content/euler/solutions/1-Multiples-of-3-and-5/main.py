T = int(input())

def triangular(n):
	return n * (n+1) // 2

def sum_under(n,m):
	return m*triangular((n-1)//m)

for _ in range(T):
	N = int(input())
	print(sum_under(N,3) + sum_under(N,5) - sum_under(N,15))