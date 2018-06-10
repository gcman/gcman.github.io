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

abundants = [i for i,x in enumerate(sigma(28123)) if x - i > i]
out = [x for x in range(28123)]

for i in abundants:
    for j in abundants:
        if i + j < 28123:
            out[i+j] = 0
        else:
            break

print(sum(out))