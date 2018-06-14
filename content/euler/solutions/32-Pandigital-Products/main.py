def perms(s):        
	if len(s) == 1:
		return [s]
	out = []
	for i,v in enumerate(s):
		out += [v+p for p in perms(s[:i]+s[i+1:])]
	return out

N = int(input())
PANDIGITAL = perms("".join(map(str,range(1,N+1))))
PROD = set()
for x in PANDIGITAL:
	for i in range(1,N):
		for j in range(i+1,N):
			if int(x[:i]) * int(x[i:j]) == int(x[j:]):
				PROD.add(int(x[j:]))
print(sum(PROD))