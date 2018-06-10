def bs(arr, l, r, x):
	while l <= r:
		mid = l + (r - l)//2;
		if arr[mid] == x:
			return arr[mid-1] # The answer must be less than N
		elif arr[mid] < x:
			l = mid + 1
		else:
			r = mid - 1
	return arr[r]

pals = set()
for i in range(100,1000):
	for j in range(100,1000):
		if str(ij) == str(ij)[::-1]:
			pals.add(i*j)
pals = sorted(list(pals))

T = int(input())
for _ in range(T):
	N = int(input())
	ans = bs(pals,0,len(pals)-1,N)
	print(ans)