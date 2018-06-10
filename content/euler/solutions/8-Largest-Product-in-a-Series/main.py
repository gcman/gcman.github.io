def substrings(s,k): # Substrings of s of length k
	out = []
	n = len(s)
	for i in range(n-k+1):
		out.append(s[i:i+k])
	return out

def string_prod(s): # Multiplies the digits in a string int
	ans = 1
	for x in s:
		ans *= int(x)
	return ans

T = int(input())
for _ in range(T):
	N,K = map(int,input().split())
	S = input().strip()
	ans = max([string_prod(x) for x in substrings(S,K)])
	print(ans)