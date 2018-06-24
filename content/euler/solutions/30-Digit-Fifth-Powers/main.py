from itertools import combinations_with_replacement
from collections import Counter
N = int(input())

DIGITS = {}
# Correspondence from x^N -> x
for x in range(10):
	DIGITS[x**N] = x

ans = 0
# No answer has more than 6 digits
for k in range(2,7):
	# Generate combinations with replacement of (0^N,...9^N)
	for candidate in combinations_with_replacement(DIGITS,k):
		# Get multiset of N-th roots of elements of combination
		digits_used = Counter(map(lambda x: DIGITS[x],candidate))
		# Candidate sum
		S = str(sum(candidate))
		# Get multiset of digits of candidate sum
		powers_used = Counter(map(int,S))
		if digits_used == powers_used:
			ans += int(S)
print(ans)