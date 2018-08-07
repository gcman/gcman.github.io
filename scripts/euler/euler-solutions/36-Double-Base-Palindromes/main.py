from math import log

# Convert decimal n to base b string
def base(n,b):
	out = ""
	# The maximal place of the first digit
	max_exponent = int(log(n,b))
	# Starting from the rightmost place ^
	for exp in range(max_exponent,-1,-1):
		# See how many times b**exp goes into n
		# Subtract it off and keep going
		out += str(n // b**exp)
		n %= b**exp
	return out

# Generate all base-10 palindromes with at most n digits
# Return only those less than upper bound m
def pals(n,m):
	# Initialize with one digit palindromes
	# Note: 0 is not natural in this problem
	PALS = [1,2,3,4,5,6,7,8,9]
	# Get all numbers with at most n/2 digits
	first_half = list(map(str,range(1,10**(n//2 + 1))))
	# This will be the 'middle of the sandwich'
	mid = "0123456789"
	# Odd-length palindromes
	# Add the first half, sandwich in the middle, reverse the first half
	PALS += [first_half[i] + x + first_half[i][::-1] for x in mid for i in range(len(first_half))]
	# Even length palindromes
	# Same as above, but without middle
	PALS += [x + x[::-1] for x in first_half]
	return [int(x) for x in PALS if int(x) < m]

N,K = map(int,input().split())
# 10-palindromes with as many digits as N less than N
P = pals(int(log(N,10)),N)
# Check if 10-palindrome is also k-palindromic
print(sum([x for x in P if base(x,K) == base(x,K)[::-1]]))