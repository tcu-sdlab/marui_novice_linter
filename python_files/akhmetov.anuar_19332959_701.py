t = input
p = print
r = range
n, m = map(int, t().split())
co = [0] * n
ro = [0] * n
cco = n
cro = n
for i in r(m):
    x, y = map(int, t().split())
    if ro[x - 1] != 1:
        ro[x - 1] = 1
        cro -= 1
    if co[y - 1] != 1:
        co[y - 1] = 1
        cco -= 1
    p(cco * cro)