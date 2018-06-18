# Get indices of adjacent entries to (i,j) in row above
def parents(i,j):
	out = []
	if j < i:
		out.append(j)
	if 0 < j:
		out.append(j-1)
	return out

def max_sum(arr):
	# The previous rows max_sums
	parent = []
	for i,row in enumerate(arr):
		curr = []
		if i == 0:
			# Handle the case where there are no parents
			curr = [row[0]]
		else:
			# Get the higher parent sum and add the current entry
			for j,elem in enumerate(row):
				curr.append(elem + max([parent[x] for x in parents(i,j)]))
		# We're done with the row
		# So move it into memory for the next row
		parent = curr
	return max(parent)

T = int(input())
for _ in range(T):
	N = int(input())
	rows = [list(map(int,input().split())) for _ in range(N)]
	ans = max_sum(rows)
	print(ans)