# Written by Gautam Manohar

def chooseMIL(n):
	ncr_temp = 1
	out = 0
	for r in range(1,n//2+1):
		ncr = ncr_temp * (n-r+1)//r
		ncr_temp = ncr
		if ncr > int(1e6):
			out += n - 2*r + 1
			break
	return out

S = sum([chooseMIL(i) for i in range(1,101)])
print(S)