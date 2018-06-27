# Use Euclid's algorithm
def gcd(a,b):
	while b:
		a,b = b,a%b
	return a