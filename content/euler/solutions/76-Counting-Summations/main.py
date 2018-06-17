P = 1000000007
dp = [0] * (1001)
dp[0] = 1
for i in range(1,1000):
	for j in range(i,1001):
		dp[j] = (dp[j] + dp[j-i]) % P
print(dp)
T = int(input())
for _ in range(T):
    N = int(input())
    print((dp[N]-1) % P)