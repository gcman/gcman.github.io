from math import log

def base(n,b):
	out = []
	kmax = int(log(n,b))
	for k in range(kmax,-1,-1):
		out.append(n // b**k)
		n %= b**k
	return "".join(map(str,out))

def pals(n,m):
	PALS = [1,2,3,4,5,6,7,8,9]
	first_half = list(map(str,range(1,10**(n//2 + 1))))
	mid = "0123456789"
	PALS += [first_half[i] + x + first_half[i][::-1] for x in mid for i in range(len(first_half))]
	PALS += [x + x[::-1] for x in first_half]
	PALS = [int(x) for x in PALS if int(x) < m]
	return PALS

N,K = map(int,input().split())
P = pals(int(log(N,10)),N)
print(sum([x for x in P if base(x,K) == base(x,K)[::-1]]))