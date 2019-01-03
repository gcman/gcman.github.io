from itertools import combinations_with_replacement
from collections import Counter
from math import factorial

DIGITS = {}
# Correspondence from n! -> n
# Precompute these to save time
for n in range(10):
	DIGITS[n] = factorial(n)

ans = 0
# Upper bound of 7 digits
for k in range(2,8):
	# Choose k elements from {0,...,9} with replacement
	for candidate in combinations_with_replacement(DIGITS,k):
		# Get multiset of candidate digits
		digits_used = Counter(map(str,candidate))
		# Calculate candidate factorial sum
		S = sum([factorial(x) for x in candidate])
		# Get multiset of digits in ^
		# Are these digit multisets the same?
		factorials_used = Counter(str(S))
		if digits_used == factorials_used:
			ans += S
print(ans)