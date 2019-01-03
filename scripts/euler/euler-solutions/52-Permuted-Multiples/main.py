# Check sorted strings
def is_perm(arr):
	return all([sorted(arr[0]) == sorted(x) for x in arr])

N,K = map(int,input().split())
# We are given N >= 125874
for i in range(125874,N+1):
	# First check that all digits are unique
	# Then check that Ki is not too long
	if len(str(i)) == len(set(str(i))) and len(str(i*K)) == len(str(i)):
		# Generate multiples
		S = [str(i*j) for j in range(1,K+1)]
		# Check that all multiples are permutations
		if is_perm(S):
			print(" ".join(S))