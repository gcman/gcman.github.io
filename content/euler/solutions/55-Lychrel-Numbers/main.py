def isPal(n):
	return str(n) == str(n)[::-1]

def lychrel(n):
	if isPal(n):
		return n
	i = 0
	while i < 60:
		i += 1
		n += int(str(n)[::-1])
		if isPal(n):
			return n
	return 0

N = int(input())
freq = {}

for n in range(1,N+1):
	res = lychrel(n)
	if res not in freq:
		freq[res] = 0
	freq[res] += 1
freq[0] = 0

print(" ".join(sorted([(str(key),str(freq[key])) for key in freq],key=lambda x: int(x[1]),reverse=True)[0]))