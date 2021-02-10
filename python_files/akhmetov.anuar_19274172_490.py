t = input
p = print
r = range
n = int(t())
a = list(map(int, t().split()))
s = {1: [], 2: [], 3: []}
for i in range(n):
    s[a[i]].append(i)

ans = min(map(lambda x: len(x), list(s.values())))
p(ans)
if ans > 0:
    for i in range(ans):
        p(s[1].pop() + 1, s[2].pop() + 1, s[3].pop() + 1)