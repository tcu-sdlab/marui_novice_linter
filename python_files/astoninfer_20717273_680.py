t = list(map(int, input().split()))
tot = 0
for i in range(1, 6):
    tot += t[i - 1]
t.sort()
ans = tot
for i in range(0, 5):
    if i + 2 < 5 and t[i + 2] == t[i]:
        ans = min(ans, tot - 3 * t[i])
    elif i + 1 < 5 and t[i + 1] == t[i]:
        ans = min(ans, tot - 2 * t[i])
print(ans)