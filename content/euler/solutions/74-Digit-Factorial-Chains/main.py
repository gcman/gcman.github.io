from math import factorial

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

# Initialize the memoization list
MAX = int(1e6)
memo = [0]*(MAX + 1)
# List of indices at which there is a new maximum
max_list = [1]
LOOP = [(1,1),(2,1),(145,1),(169,4),(871,3),(872,3),(40585,1)]
FREQ = {}

for x in LOOP:
	memo[x[0]] = x[1]
	FREQ[x[1]] = [x[0]]

def factorial_sum(n):
	return sum([factorial(int(x)) for x in str(n)])

def chain(n):
	out = [n]
	while out[-1] >= MAX or memo[out[-1]] == 0:
		out.append(factorial_sum(out[-1]))
	extra = memo[out[-1]]
	del out[-1]
	for i,x in enumerate(out):
		if x <= MAX:
			memo[x] = len(out) + extra - i
			if memo[x] not in FREQ:
				FREQ[memo[x]] = []
			FREQ[memo[x]].append(x)

def get_freq(n,l):
	FREQ[l] = sorted(FREQ[l])
	idx = bs(FREQ[l],0,len(FREQ[l])-1,n)
	return " ".join([str(x) for x in FREQ[l][:idx]])

for i in range(3,MAX+1):
	if memo[i] == 0:
		chain(i)

T = int(input())
for _ in range(T):
	N,L = map(int,input().split())
	print(get_freq(N,L))