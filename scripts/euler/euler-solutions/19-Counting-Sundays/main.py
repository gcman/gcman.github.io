def leap_year(y):
	if y % 4 == 0:
		if y % 100 == 0:
			if y % 400 == 0:
				return True
			return False
		return True
	return False

def days_in_month(y,m):
	if m in [4,6,9,11]:
		return 30
	elif m == 2:
		if leap_year(y):
			return 29
		return 28
	return 31

def days_since(y,m,d):
	leaps = y//4 - y//100 + y//400 - 498 # 498 leap years from 0-1900
	month_days = sum([days_in_month(y,month) for month in range(1,m+1)])
	days = d - 1
	years = y - 1900
	return years*365 + leaps + month_days + days

def next_month(y,m,d):
	if m == 12:
		return y+1,1,d
	return y,m+1,d

def firsts_in_range(y,m,d,y2,m2,d2):
	count = 0
	if d != 1:
		d = 1
		if m == 12:
			m = 1
			y += 1
		else:
			m += 1
	DAYS = days_since(y,m,d)
	begin = (y,m,d)
	if d2 != 1:
		d2 = 1
	end = (y2,m2,d2)
	while DAYS <= days_since(y2,m2,d2):
		if DAYS % 7 == 6: # Sunday is 6 days after Monday, the first day
			count += 1
		DAYS += days_in_month(y,m)
		y,m,d = next_month(y,m,d)
	return count

T = int(input())
for _ in range(T):
	Y1,M1,D1 = map(int,input().split())
	Y2,M2,D2 = map(int,input().split())
	print(firsts_in_range(Y1,M1,D1,Y2,M2,D2))