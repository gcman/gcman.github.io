def loc(n):
	fact = 9
	count = 1
	while n - fact*count > 0 and fact*count < 9*10**18:
		n -= fact*count
		fact *= 10
		count += 1
	return n-1,count

def digit(n):
	pos,count = loc(n)
	dig = int(str(10**(count-1)+pos//count)[pos%count])
	return dig

def dig_prod(arr):
	out = 1
	for x in arr:
		out *= digit(x)
	return out

T = int(input())
for _ in range(T):
	D = map(int,input().split())
	print(dig_prod(D))