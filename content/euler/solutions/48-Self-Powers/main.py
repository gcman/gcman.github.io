N = int(input())
M = 10**10
S = 0
for n in range(1,N+1):
	# Take powers mod 10^10
	# Mod 10^10 at the end
	S = (S + pow(n,n,M))%M
print(S)