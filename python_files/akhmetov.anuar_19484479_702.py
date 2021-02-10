t = input
p = print
r = range
n = int(t())
a = list(map(int, t().split()))

for i in range(1, n):
    if a[i] > a[i - 1]:
        a[i - 1] = 1
    else:
        a[i - 1] = 0

if a[n - 1] > a[n - 2]:
    a[n - 1] = 1
else:
    a[n - 1] = 0

ma = 0
c = 0
for i in range(n):
    if a[i] == 1:
        c += 1
    else:
        c += 1
        ma = max(ma, c)
        c = 0
    ma = max(ma, c)
p(ma)