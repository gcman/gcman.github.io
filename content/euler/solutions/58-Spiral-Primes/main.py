def try_composite(a,d,n,s):
	if pow(a,d,n) == 1:
		return False
	for i in range(s):
		if pow(a,2**i*d,n) == n-1:
			return False
	return True
 
def is_prime(n,precision_for_huge_n=16):
	if n in known_primes or n in (0,1):
		return True
	if any((n % p) == 0 for p in known_primes):
		return False
	d,s = n - 1,0
	while not d % 2:
		d,s = d >> 1,s + 1
	if n < 1373653: 
		return not any(try_composite(a,d,n,s) for a in (2,3))
	if n < 25326001: 
		return not any(try_composite(a,d,n,s) for a in (2,3,5))
	if n < 118670087467: 
		if n == 3215031751: 
			return False
		return not any(try_composite(a,d,n,s) for a in (2,3,5,7))
	if n < 2152302898747: 
		return not any(try_composite(a,d,n,s) for a in (2,3,5,7,11))
	if n < 3474749660383: 
		return not any(try_composite(a,d,n,s) for a in (2,3,5,7,11,13))
	if n < 341550071728321: 
		return not any(try_composite(a,d,n,s) for a in (2,3,5,7,11,13,17))
	return not any(try_composite(a,d,n,s) for a in known_primes[:precision_for_huge_n])
 
known_primes = [2,3]
known_primes += [x for x in range(5,1000,2) if is_prime(x)]

n = 1
p = 0
N = int(input())
while True:
	n += 2
	p += sum([is_prime(x) for x in [n**2 - i*(n-1) for i in range(1,4)]])
	if 100*p/(2*n - 1) < N:
		break
print(n)