def dig_sum(n):
	return sum([int(x) for x in str(n)])

N = int(input())
print(max([dig_sum(a**b) for a in range(1,N) for b in range(1,N)]))