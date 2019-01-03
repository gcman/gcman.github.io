from math import log

N = int(input())
exp = [tuple(map(int,input().split())) for _ in range(N)]
exp = sorted(exp,key = lambda x: x[1]*log(x[0]))
K = int(input())
print(exp[K-1][0],exp[K-1][1])