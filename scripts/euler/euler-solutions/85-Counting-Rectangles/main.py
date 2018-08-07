from math import sqrt

def triangle(n):
	return n*(n+1)//2

def rectangles(m,n):
	return triangle(m)*triangle(n)

def closest_match(n):
	closest = n
	best_area = 0
	for x in range(1,int(sqrt(n))+1):
		y = x
		count = 0
		while count < n:
			count = rectangles(x,y)
			error = abs(n-count)
			area = x*y
			if error < closest:
				closest = error
				best_area = area
			elif error == closest and best_area < area:
				best_area = area
			y += 1
	return best_area

T = int(input())
for _ in range(T):
	N = int(input())
	print(closest_match(N))