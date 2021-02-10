t = input
p = print
r = range
n, a = int(t()), list(map(int, t().split()))
m, b = int(t()), list(map(int, t().split()))
f = [0]
for i in range(n):
    f += [i + 1] * a[i]
for x in b:
    p(f[x])