# Written by Gautam Manohar

S = []
for a in range(1,100):
	for b in range(1,100):
		S.append(sum([int(x) for x in str(a**b)]))
print(max(S))