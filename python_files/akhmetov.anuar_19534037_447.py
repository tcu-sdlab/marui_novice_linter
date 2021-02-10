t = input
r = range
p = print
s = t()
k = int(t())
w = list(map(int, t().split()))
ans = 0
ma = max(w)
for i in r(len(s)):
    ans += w[ord(s[i]) - 97] * (i + 1)
su = 0
for i in range(len(s), len(s) + k):
    su += (i + 1) * ma
p(ans + su)