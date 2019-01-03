# Substrings of s of length k
def substrings(s,k):
	out = []
	n = len(s)
	for i in range(n-k+1):
		out.append(s[i:i+k])
	return out

# Multiplies the digits in a string int
def string_prod(s):
	ans = 1
	for x in s:
		ans *= int(x)
	return ans

T = int(input())
for _ in range(T):
	N,K = map(int,input().split())
	S = input().strip()
	# Brute force each substring
	ans = max([string_prod(x) for x in substrings(S,K)])
	print(ans)