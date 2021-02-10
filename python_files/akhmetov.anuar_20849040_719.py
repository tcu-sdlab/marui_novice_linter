t = input
p = print
r = range
n = int(t())
a = list(map(int, t().split()))
ans = -1
if n > 1:
    last = a[-1]
    pre_last = a[-2]
    if last > pre_last:
        ans = "UP"
    else:
        ans = "DOWN"
    if last == 0 and pre_last == 1:
        ans = "UP"

    if last == 15 and pre_last == 14:
        ans = "DOWN"
else:
    if a[0] == 0:
        ans = "UP"
    if a[0] == 15:
        ans = "DOWN"


print(ans)