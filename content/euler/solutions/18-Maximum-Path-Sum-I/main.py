def parents(i,j):
	out = []
	if j < i:
		out.append(j)
	if 0 < j:
		out.append(j-1)
	return out

def max_sum(arr):
	parent = []
	for i,row in enumerate(arr):
		curr = []
		if i == 0:
			curr = [row[0]]
		else:
			for j,elem in enumerate(row):
				curr.append(elem + max([parent[x] for x in parents(i,j)]))
		parent = curr
	return max(parent)

T = int(input())
for _ in range(T):
	N = int(input())
	rows = [list(map(int,input().split())) for _ in range(N)]
	ans = max_sum(rows)
	print(ans)