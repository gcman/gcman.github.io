#Written by Arif Aulakh
import math
def isprime(n):
	for i in range(2,int(math.sqrt(n)+1)):
		if n%i == 0:
			return False
	return True
primes = []
num =1	
while True:
	num +=1
	if isprime(num):
		primes.append(num)
	if len(primes) == 10001:
		print(primes[10000])
		break

