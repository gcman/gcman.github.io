def count(coins,n):
	dp = [0 for _ in range(n+1)]
	dp[0] = 1
	for coin in coins:
		for val in range(coin,n+1):
			dp[val] = (dp[val] + dp[val-coin]) % 1000000007
	return dp

COINS = [1,2,5,10,20,50,100,200]
COUNT = count(COINS,int(1e5))
T = int(input())
for _ in range(T):
	N = int(input())
	print(COUNT[N])