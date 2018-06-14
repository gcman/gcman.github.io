from math import log

def truncatable_primes(n):
	S = 0
	primes = []
	sieve = [True] * (n + 1)
	sieve[1] = False
	for p in range(2, n + 1):
		if sieve[p]:
			primes.append(p)
			for i in range(p * p, n + 1, p):
				sieve[i] = False
			if p > 10:
				right = p
				while right > 0 and sieve[right]:
					right //= 10
				left = p
				digit = 1
				while 10*digit <= left:
					digit *= 10
				while left > 0 and sieve[left]:
					left %= digit
					digit //= 10
				if left == 0 and right == 0:
					S += p
	return S

N = int(input())
print(truncatable_primes(N))