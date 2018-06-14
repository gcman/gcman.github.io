def pow_sum(n,power):
	out = 0
	for x in str(n):
		out += pow(int(x),power)
	return out

N = int(input())
S = 0
for i in range(10,8*9**6+1):
	if pow_sum(i,N) == i:
		S += i
print(S)