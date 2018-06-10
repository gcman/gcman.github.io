# Written by Gautam Manohar and Arif Aulakh

with open("data.in","r") as f:
	S = 0
	for line in f:
		S += int(line)
print(str(S)[:10])