from math import sqrt

def gcd(a,b):
	while b:
		a, b = b, a%b
	return a

# Binary search
def bs(arr, l, r, x):
	while l <= r:
		mid = l + (r - l)//2;
		if arr[mid] == x:
			return mid
		elif arr[mid] < x:
			l = mid + 1
		else:
			r = mid - 1
	return r

MAX = int(5e6)
maxm = int(sqrt(MAX//2))

# pythag[p] = no. of sols for perimeter p
pythag = [0] * (MAX + 1)
# Don't need to search m = 0 or n = 0
# ^ Isoceles right triangle with hypotenuse = k*sqrt(2)
for m in range(1,maxm):
	# Make sure m > n
	for n in range(1,m+1):
		P = 2*m*(m+n)
		# Check three conditions for primitive pythag trip
		if P <= MAX and (m+n) % 2 == 1 and gcd(m,n) == 1:
			# For each multiple of the PPT, count one more sol
			for k in range(1,MAX//P + 1):
				pythag[k*P] += 1

# Find indices of perims with only one sol
singular = [0]
for i,x in enumerate(pythag):
	if x == 1:
		singular.append(i)

T = int(input())
for _ in range(T):
	N = int(input())
	# Binary search for answer.
	print(bs(singular,0,len(singular)-1,N))