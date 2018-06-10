# Written by Gautam Manohar and Arif Aulakh

ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open("names.txt","r") as f:
	names = sorted(f.readline().split(","))
	S = 0
	for i,n in enumerate(names):
		SINT = 0
		for char in n:
			if char in ALPH:
				SINT += ALPH.index(char)+1
		S += (i+1)*SINT
print(S)	