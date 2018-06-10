import math

fib = [1,1]
max = 4e6
phi = (1 + math.sqrt(5))/2
n = int(math.log(math.sqrt(5)*max, phi))

for i in range(2,n+1):
	fib.append(fib[i-1]+fib[i-2])

print(sum([fib[i] for i in range(2,n+1,3)]))