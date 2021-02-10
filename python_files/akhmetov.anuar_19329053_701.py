t = input
p = print
r = range
n = int(t())
a = list(map(int, t().split()))
ma = max(a)
mi = min(a)
su = mi + ma
for i in range(n):
    if a[i] == -1:
        continue
    else:
        for j in range(n):
            if a[i] + a[j] == su and i != j:
                p(i + 1, j + 1)
                a[i] = -1
                a[j] = -1