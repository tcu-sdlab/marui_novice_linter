t = input
p = print
r = range
n = int(t())
a = list(map(int, t().split()))
c = 0
co = {x: 0 for x in range(1000000)}
po = [2 ** x for x in range(33)]
for i in range(n):
    if a[i] in co:
        c += co.get(a[i])
    for j in range(len(po)):
        if a[i] < po[j]:
            co.update({po[j] - a[i]: co.get(po[j] - a[i], 0) + 1})
p(c)