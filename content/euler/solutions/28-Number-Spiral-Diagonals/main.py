P = 1000000007

def inv(a, m):
	return pow(a,m-2,m)

def diag_sum(n):
	return ((4*pow(n,3,P) + 3*pow(n,2,P) + 8*n - 9)*inv(6,P)) % P

T = int(input())
for _ in range(T):
	N = int(input())
	print(diag_sum(N))