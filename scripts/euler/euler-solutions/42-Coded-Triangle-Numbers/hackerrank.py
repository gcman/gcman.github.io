def is_triangular(n):
	inv = (-1+(1+8*n)**0.5)/2
	status = inv == int(inv)
	if not status:
		inv = -1
	return int(inv)

T = int(input())
for _ in range(T):
	N = int(input())
	print(is_triangular(N))