from math import sqrt

# Compute the sum of divisors
def divisor_sum(n):
	s = 0
	for i in range(1,int(sqrt(n))+1):
		if n % i == 0:
			s += i
			if i != n//i:
				s += n//i
	return s - n

MAX = int(1e5)
# Precompute all amicable numbers
AMICABLE = []
for x in range(1,MAX+1):
	friend = divisor_sum(x)
	# Check if x = d(d(x)) and x != d(x)
	if x == divisor_sum(friend) and x != friend:
		# Avoid duplicates
		if x not in AMICABLE:
			AMICABLE.append(x)

T = int(input())
for _ in range(T):
	N = int(input())
	S = sum([x for x in AMICABLE if x < N])
	print(S)