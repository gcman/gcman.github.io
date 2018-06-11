def prod(arr):
	ans = 1
	for x in arr:
		ans *= x
	return ans

G = [list(map(int,input().split())) for _ in range(20)]
ans = 0
for y in range(20):
	for x in range(20):
		if x < 17:
			horiz = prod([G[x+i][y] for i in range(4)])
		else:
			horiz = 0
		if y < 17:
			vert = prod([G[x][y+i] for i in range(4)])
		else:
			vert = 0
		if x < 17 and y < 17:
			ldiag = prod([G[x+i][y+i] for i in range(4)])
		else:
			ldiag = 0
		if x >= 3 and y < 17:
			rdiag = prod([G[x-i][y+i] for i in range(4)])
		else:
			rdiag = 0
		ans = max(ans,horiz,vert,ldiag,rdiag)
print(ans)