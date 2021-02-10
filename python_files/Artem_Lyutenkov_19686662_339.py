n, m = map(int, input().split())
t = 1
ans = 0
for i in map(int, input().split()):
    ans += (i - t) % n
    t = i
print(ans)