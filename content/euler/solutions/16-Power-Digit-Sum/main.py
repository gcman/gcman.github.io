def digit_sum(n):
	s = 0
	while n > 0:
		s += n % 10
		n = (n - n%10) // 10
	return s

T = int(input())
for _ in range(T):
	N = int(input())
	print(digit_sum(pow(2,N)))