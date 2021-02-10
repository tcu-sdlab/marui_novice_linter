t = input
p = print
r = range
a = list(map(int, t().split()))
ans = 0
if a[0] == a[1] == a[2] or max(a) - min(a) == 1:
    ans = 0
elif min(a) == 0:
    mid = sorted(a)[1]
    diff = 1 if max(a) == mid else 2
    ans = max(a) * 2 - mid - diff
else:
    a = list(map(lambda x: x - min(a), a))
    mid = sorted(a)[1]
    diff = 1 if max(a) == mid else 2
    ans = max(a) * 2 - mid - diff
p(ans)