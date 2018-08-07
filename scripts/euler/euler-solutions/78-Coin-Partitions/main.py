def sgn(n):
		return 1 if (n//2)%2 == 0 else -1

def pent(n):
	out = [1]
	i = 1
	sign = True
	while out[-1] <= n:
		i += 1
		sign = not sign
		k = i//2*(-1)**int(sign)
		out.append(k*(3*k - 1)//2)
	del out[0]
	return out

MAX = int(6e4)
PENT = pent(MAX)
PART = [0] * (MAX +1)
PART[0] = 1
# Report ans mod 10^9 + 7
P = 1000000007

for n in range(MAX+1):
	for i,p in enumerate([x for x in PENT if x <= n]):
		PART[n] += sgn(i)*PART[n-p]
	PART[n] %= P

T = int(input())
for _ in range(T):
	N = int(input())
	print(PART[N])