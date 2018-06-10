# Written by Gautam Manohar
def fib():
	a = 0
	b = 1
	while True:
		yield b
		a,b = b,a+b
f = enumerate(fib())
n = 0
while len(str(n)) < 1000:
	i,n = next(f)
print(i+1)