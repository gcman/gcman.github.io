# Returns the number of entries
# in the n-th row of Pascal's triangle
# greater than K
def choose_max(n,k):
	# The current binomial coefficient
	curr = 1
	# Go up to the central coefficient
	for i in range(n//2+(n+1)%2):
		if curr > k:
			# Count all the entries from i to n-i
			return n + 1 - 2*i
		# Recurrence relation for next coeff
		curr *= n - i
		curr //= i + 1
	# No entries > K were found
	return 0

N,K = map(int,input().split())
# Add up all the rows up to N
print(sum([choose_max(n,K) for n in range(1,N+1)]))