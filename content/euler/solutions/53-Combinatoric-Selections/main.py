def choose_max(n,k):
	curr = 1
	for i in range(n//2+(n+1)%2):
		if curr > k:
			return n + 1 - 2*i
		curr *= n - i
		curr //= i + 1
	return 0

N,K = map(int,input().split())
print(sum([choose_max(n,K) for n in range(1,N+1)]))