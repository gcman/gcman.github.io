from itertools import permutations

def gcd(a,b):
	while b:
		a, b = b, a%b
	return a

def fill_in(empty,extra):
	empty = list(empty)
	extra = list(str(extra))
	for i in range(len(extra)):
		empty[empty.index("-")] = extra[i]
	return int("".join(list(empty)))

original = set()

N,K = map(int,input().split())
blanks = "".join(["-" for _ in range(K)])
for den in range(1,10**(N-K)):
	den_perms = list(permutations(blanks + str(den)))
	for num in range(1,den):
		num_perms = list(permutations(blanks + str(num)))
		for x in num_perms:
			for y in den_perms:
				for extra in range(10**(K-1),10**K):
					NUM = fill_in(x,extra)
					DEN = fill_in(y,extra)
					if NUM*den == num*DEN and "0" not in str(extra):
						original.add((NUM,DEN))

num_sum = 0
den_sum = 0
for frac in original:
	num_sum += frac[0]
	den_sum += frac[1]

print(num_sum,den_sum)