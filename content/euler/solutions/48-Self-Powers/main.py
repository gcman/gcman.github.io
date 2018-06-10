# Written by Gautam Manohar
M = 10**10
S = 0
for i in range(1,1001):
	S = (S + pow(i,i,M)) % M
print(S)