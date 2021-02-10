s = list(map(int, input().split()))
d = dict()
for i in s:
    if i not in d:
        d[i] = 0
    d[i] += 1
sm = sum(s)
ans = sm
for i in d.items():
    if i[1] >= 2:
        ans = min(ans, sm - i[0] * min(i[1], 3))
print(ans)