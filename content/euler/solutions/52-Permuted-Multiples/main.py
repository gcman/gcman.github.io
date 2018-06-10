# Written by Gautam Manohar

def digits(n):
	res = set([])
	while n != 0:
		res.add(n%10)
		n //= 10
	return res

i = 0
while True:
	i += 1
	S = digits(i)
	if len(S) == len(digits(2*i).union(digits(3*i)).union(digits(4*i)).union(digits(5*i)).union(digits(6*i))):
		break
print(i)