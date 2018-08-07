MOD = pow(10,12)

def main(a,b,c,d):
	ans = ((a*pow(b,c,MOD)) % MOD + d) % MOD
	return ans

S = 0
T = int(input())
for _ in range(T):
	A,B,C,D = map(int,input().split())
	S = (S + main(A,B,C,D)) % MOD

S = "".join(["0" for _ in range(12 - len(str(S)))]) + str(S)
print(S)