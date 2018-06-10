# Written by Gautam Manohar

def rev(n):
	R = 0
	while n > 0:
		digit = n % 10
		R = R*10 + digit
		n //= 10
	return R

def isPal(n):
	return n == rev(n)

def isLychrel(n):
	i = 0
	while i < 50:
		i += 1
		n += rev(n)
		if isPal(n):
			return True
	return False

S = sum([not isLychrel(n) for n in range(1,10001)])
print(S)