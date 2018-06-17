def gcd(a,b):
	while b:
		a, b = b, a%b
	return a

def bs(arr, l, r, x):
	while l <= r:
		mid = l + (r - l)//2;
		if arr[mid] == x:
			return arr[mid]
		elif arr[mid] < x:
			l = mid + 1
		else:
			r = mid - 1
	return arr[r]

MAX = int(5e6)
pythag = [0] * (MAX + 1)
for m in range(1,1581):
	for n in range(1,m+1):
		P = 2*m*(m+n)
		if P <= MAX and (m+n) % 2 == 1 and gcd(m,n) == 1:
			for k in range(1,MAX//P+1):
				pythag[k*P] += 1
freq = [0]
for i,x in enumerate(pythag):
	if x > pythag[freq[-1]]:
		freq.append(i)
del freq[0]

T = int(input())
for _ in range(T):
	N = int(input())
	print(bs(freq,0,len(freq)-1,N))