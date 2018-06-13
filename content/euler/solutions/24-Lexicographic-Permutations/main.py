from math import factorial

def lex_perm(n,s):
	n %= factorial(len(s))
	indices = []
	for x in range(len(s)-1,-1,-1):
		elem = n // factorial(x)
		indices.append(elem)
		n -= elem * factorial(x)
	s = sorted(list(s))
	out = ""
	for i in indices:
		out += s[i]
		del s[i]
	return out


S = "abcdefghijklm"
T = int(input())
for _ in range(T):
	N = int(input())-1
	print(lex_perm(N,S))