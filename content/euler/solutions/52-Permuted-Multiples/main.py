def is_perm(arr):
	return all([sorted(arr[0]) == sorted(x) for x in arr])

N,K = map(int,input().split())
for i in range(125874,N+1):
	if len(str(i)) == len(set(str(i))) and len(str(i*K)) == len(str(i)):
		S = [str(i*j) for j in range(1,K+1)]
		if is_perm(S):
			print(" ".join(S))