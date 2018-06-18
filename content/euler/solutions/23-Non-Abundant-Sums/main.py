from math import sqrt

# Find sum of divisors of n
def divisor_sum(n):
	s = 0
	for i in range(1,int(n**0.5)+1):
		if n % i == 0:
			s += i
			if i != n//i:
				s += n//i
	return s - n

# We don't need to go past this
MAX = 28123
ABUNDANT = set()
for i in range(1,MAX+1):
	if i < divisor_sum(i):
		ABUNDANT.add(i)

def abundant_sum(n):
	if n > 28123:
		return True
	# Find all the differences
	diff = set(n - x for x in ABUNDANT)
	# Check if any of these differences are abundant
	if diff & ABUNDANT:
		return True
	return False

T = int(input())
for _ in range(T):
	N = int(input())
	if abundant_sum(N):
		print("YES")
	else:
		print("NO")