from collections import Counter

t = input
p = print
r = range
k = int(t())
s = Counter(t())
ans = -1

ok = True
for key in s.keys():
    if s[key] % k != 0:
        ok = False
        break
if ok:
    ans = ''
    for key in s.keys():
        ans += (str(key) * (s[key] // k))
    ans *= k
p(ans)