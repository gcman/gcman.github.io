# Sieve of Eratosthenes
def primes(n):
	primes = []
	sieve = [True] * (n + 1)
	for p in range(2, n + 1):
		if sieve[p]:
			primes.append(p)
			for i in range(p * p, n + 1, p):
				sieve[i] = False
	return primes

def count(coins,n):
	# Initialize dp array
	dp = [0] * (n+1)
	# There is only one way to make nothing
	dp[0] = 1
	for coin in coins:
		for val in range(coin,n+1):
			dp[val] += dp[val-coin]
	return dp

# N <= 1000
P = primes(1000)
COUNT = count(P,1000)
T = int(input())
for _ in range(T):
	N = int(input())
	print(COUNT[N])