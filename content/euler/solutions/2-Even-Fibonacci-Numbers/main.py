def next_even(f):
	return 4*f[1] + f[0]

def even_fib_sum(n):
	fib = [0,2]
	if n >= 2:
		count = 2
	else:
		count = 0
	while next_even(fib) <= n:
		count += next_even(fib)
		fib = [fib[1],next_even(fib)]
	return count

T = int(input())
for _ in range(T):
	N = int(input())
	print(even_fib_sum(N))