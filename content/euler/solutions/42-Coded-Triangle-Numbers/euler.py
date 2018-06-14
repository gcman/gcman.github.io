ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def is_triangular(n):
	inv = (-1+(1+8*n)**0.5)/2
	status = inv == int(inv)
	if not status:
		inv = -1
	return inv

def score(s):
	return sum([ALPH.index(x) + 1 for x in s])

with open("words.txt","r") as f:
	words = f.readline().split(",")
	words = [x.replace('"',"") for x in words]
count = 0
for x in words:
	if is_triangular(score(x)) != -1:
		count += 1
print(count)