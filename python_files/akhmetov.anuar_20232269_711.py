t = input
p = print
r = range
n = int(t())
a = [''] * n
ans = "NO"
for i in r(n):
    s = t()
    if 'OO' in s and ans == "NO":
        ans = "YES"
        s = s.replace("OO", "++", 1)
    a[i] = s
print(ans)
if ans == "YES":
    for mya in a:
        p(mya)