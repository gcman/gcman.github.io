# Written by Gautam Manohar

SEQ = set([])
for a in range(2,101):
	for b in range(2,101):
		SEQ.add(a**b)
print(len(SEQ))