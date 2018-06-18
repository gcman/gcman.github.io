from math import factorial

# Returns the n-th lexicographic permutation of s
def lex_perm(n,s):
	# Write s in 'factorial base'
	n %= factorial(len(s))
	indices = []
	# Start with big factorials and subtract
	for x in range(len(s)-1,-1,-1):
		elem = n // factorial(x)
		indices.append(elem)
		n -= elem * factorial(x)
	s = sorted(list(s))
	out = ""
	for i in indices:
		# Remove the i-th remaining element
		# i is the coeffcient in the
		# factorial base expansion of n
		out += s.pop(i)
	return out

S = "abcdefghijklm"
T = int(input())
for _ in range(T):
	N = int(input())-1
	print(lex_perm(N,S))