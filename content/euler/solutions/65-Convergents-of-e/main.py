def coeff(n):
	if n == 0:
		return 2
	elif n % 3 == 2:
		return 2*(n+1)//3
	return 1

CONV = [1,coeff(0)]
N = int(input())
for i in range(2,N+1):
	next_term = coeff(i-1)*CONV[i-1] + CONV[i-2]
	CONV.append(next_term)
print(sum([int(x) for x in str(CONV[N])]))