from itertools import permutations

N = int(input())

# Get all pandigital numbers
PANDIGITAL = permutations("".join(map(str,range(1,N+1))))
# Use set to avoid duplicates
PROD = set()
for perm in PANDIGITAL:
	# Split into 3 parts
	# Make sure end of second part is after beginning
	# j > i
	for i in range(1,N):
		for j in range(i+1,N):
			x = "".join(perm)
			# Check if three parts in order are valid
			if int(x[:i]) * int(x[i:j]) == int(x[j:]):
				PROD.add(int(x[j:]))
print(sum(PROD))