t, s, x = map(int, input().split())
ok = "NO"
if t <= x:
    k = x - t
    if t == x or k % s == 0 or k % s == 1:
        ok = "YES"
    if k == 1 and s > 1:
        ok = "NO"
print(ok)