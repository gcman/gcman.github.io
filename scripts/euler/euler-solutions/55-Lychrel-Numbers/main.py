# Test if n is palindromic
def is_pal(n):
	return str(n) == str(n)[::-1]

# Find the number to which n converges
def pal_result(n):
	# palindromes covnerge to themselves
	if is_pal(n):
		return n
	i = 0
	# Iterate at most 60 times
	while i < 60:
		i += 1
		n += int(str(n)[::-1])
		# Return the palindrome, if found
		if is_pal(n):
			return n
	# Return 0 if we use 60 iterations
	return 0

N = int(input())
freq = {}

for n in range(1,N+1):
	res = pal_result(n)
	if res not in freq:
		freq[res] = 0
	# For each k that converges to n,
	# add 1 to the entry corresponding to n
	freq[res] += 1
# Remove all suspected Lychrel numbers from count
freq[0] = 0

# Get (pal, count) pairs
# Sort pairs by count in decreasing order
# Get first pair
pals = [(x,freq[x]) for x in freq]
pals = sorted(pals, key=lambda t: t[1], reverse=True)[0]
print("{} {}".format(pals[0],pals[1]))