def sigma(n):
    out = [1] * (n + 1)
    out[0] = 0
    for x in range(2,n + 1):
        if out[x] == 1:
            p,last = x,1
            while p < n + 1:
                k = last + p
                for i in range(p, n + 1, p):
                    out[i] //= last
                    out[i] *= k
                last = k
                p *= x
    return out

out = set([])

N = 10000
S = [x - i for i,x in enumerate(sigma(N))]

for i in range(N):
    for j in range(N):
        if S[i] == j and S[j] == i and i != j:
            out.add(i)
            out.add(j)
print(sum(out))