# Report ans mod 10^9 + 7
P = 1000000007
# Create dp table
dp = [0] * (1001)
# There is 1 way to partition nothing
dp[0] = 1
# "Coins" are 1...1000
for i in range(1,1001):
	for j in range(i,1001):
		dp[j] += dp[j-i]

T = int(input())
for _ in range(T):
	N = int(input())
	# Exclude case with just N
	print((dp[N] - 1) % P)