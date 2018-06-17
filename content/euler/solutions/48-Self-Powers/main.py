N = int(input())
M = 10**10
S = 0
for n in range(1,N+1):
	S = (S + pow(n,n,M))%M
print(S)