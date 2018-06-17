from collections import Counter
from itertools import combinations,product

def gcd(a,b):
	while b:
		a, b = b, a%b
	return a

def indices(s,d):
	return [i for i,dig in enumerate(s) if dig == d]

def cancellable(num,den):
	num,den = Counter(str(num)),Counter(str(den))
	out = num & den
	del out["0"]
	return list(out.elements())

def cancel_combs(num,den,k):
	num,den = str(num),str(den)
	out = []
	for x in combinations(cancellable(num,den),k):
		dig_comb = []
		for d in x:
			dig_comb.append(list(product(indices(num,d),indices(den,d))))
		out += list(product(*dig_comb))
	out = [x for x in out if all([len(set(y[i] for y in x)) == k for i in range(2)])]
	return out

def cancel(num,den,k):
	combs = cancel_combs(num,den,k)
	num,den = list(str(num)),list(str(den))
	out = set()
	for i,x in enumerate(combs):
		num_repl = [repl[0] for repl in x]
		den_repl = [repl[1] for repl in x]
		n,d = list(num),list(den)
		for idx in num_repl:
			n[idx] = "z"
		for idx in den_repl:
			d[idx] = "z"
		n = int("".join(n).replace("z",""))
		d = int("".join(d).replace("z",""))
		if n != 0 and d != 0:
			out.add((n,d))
	return out

def fake_fraction(num,den,k):
	G = gcd(num,den)
	orig = (num // G,den // G)
	for cand in cancel(num,den,k):
		GC = gcd(cand[0],cand[1])
		if (cand[0]//GC,cand[1]//GC) == orig:
			return True
	return False

N,K = map(int,input().split())
S = [0,0]
for DEN in range(10**(N-1),10**N):
	for NUM in range(10**(N-1),DEN):
		if fake_fraction(NUM,DEN,K):
			S[0] += NUM
			S[1] += DEN
print("{} {}".format(S[0],S[1]))