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

# Initialize the memoization list
MAX = int(5e6)
memo = [0]*(MAX + 1)
memo[1] = 1
# List of indices at which there is a new maximum
max_list = [1]

def collatz(n):
	# Store chain length of small n in memory
	if n <= MAX:
		if memo[n] == 0:
			if n % 2 == 0:
				# Use bitshift by 1 for speed
				memo[n] = collatz(n>>1) + 1
			else:
				memo[n] = collatz(3*n+1) + 1
		return memo[n]
	# Otherwise compute on the fly
	elif n % 2 == 0:
		return collatz(n>>1) + 1
	return collatz(3*n+1) + 1

for i in range(2,MAX+1):
	collatz(i)
	# Track right-maximal indices
	if memo[i] >= memo[max_list[-1]]:
		max_list.append(i)

T = int(input())
for _ in range(T):
	N = int(input())
	print(bs(max_list,0,len(max_list)-1,N))