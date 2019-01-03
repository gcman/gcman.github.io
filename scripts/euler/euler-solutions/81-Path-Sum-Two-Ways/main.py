N = int(input())
G = [list(map(int,input().split())) for _ in range(N)]

for i in range(N-2,-1,-1):
	G[N-1][i] += G[N-1][i+1]
	G[i][N-1] += G[i+1][N-1]

for i in range(N-2,-1,-1):
	for j in range(N-2,-1,-1):
		G[i][j] += min(G[i+1][j],G[i][j+1])

print(G[0][0])