from math import log

# Modified Sieve of Eratosthenes
def truncatable_primes(n):
	S = 0
	primes = []
	sieve = [True] * (n + 1)
	sieve[1] = False
	for p in range(2, n + 1):
		if sieve[p]:
			# When a prime is found, mark all its multiples
			for i in range(p * p, n + 1, p):
				sieve[i] = False
			# Make sure it's truncatable (2,3,5,7 are not)
			if p > 10:
				# Right truncations
				# Chop off rightmost digit as long as truncation is prime
				right = p
				while right > 0 and sieve[right]:
					right //= 10
				# Left truncations
				left = p
				# Get leftmost digit
				digit = 1
				while 10*digit <= left:
					digit *= 10
				# Chop off leftmost dig until truncation is not prime
				while left > 0 and sieve[left]:
					left %= digit
					digit //= 10
				# Is nothing left after right and left truncations?
				# Incomplete truncation -> non-truncatable prime
				if left == 0 and right == 0:
					S += p
	return S

N = int(input())
print(truncatable_primes(N))