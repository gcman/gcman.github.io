P = 1000000007

# Modular inverse
# Fermat's Little Theorem
def inv(a, m):
	return pow(a,m-2,m)

def choose(n,k):
	ans = 1
	# Recurrence in eq. (2)
	for i in range(k):
		ans = (ans * (n-i) * inv(i+1,P)) % P
	return ans

T = int(input())
for _ in range(T):
	N,M = map(int,input().split())
	print(choose(N+M,min(N,M)))