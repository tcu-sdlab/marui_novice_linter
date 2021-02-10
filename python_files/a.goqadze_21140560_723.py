a = sorted(list(map(int, input().split())))
ans = 1000
for k in range(a[0], a[2]):
    ans = min(ans, abs(k - a[0]) + abs(k - a[1]) + abs(k - a[2]))
print(ans)