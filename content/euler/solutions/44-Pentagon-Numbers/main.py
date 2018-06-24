# n-th pentagonal number
def pent(n):
	return (3*n*n - n)//2

# Inverse of pent(n)
def is_pent(n):
	inv = (1+(24*n+1)**0.5)/6
	return inv == int(inv)

N,K = map(int,input().split())
out = set()
for n in range(K+1,N+1):
	a,b = pent(n),pent(n-K)
	if is_pent(a-b) or is_pent(a+b):
		out.add(a)
for x in sorted(out):
	print(x)