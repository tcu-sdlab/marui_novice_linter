n, d = map(int, input().split())
ans = 0
cons = 0
for _ in range(d):
    s = input()
    if s == '1' * n:
        cons = 0
    else:
        cons += 1
        ans = max(ans, cons)

print(ans)