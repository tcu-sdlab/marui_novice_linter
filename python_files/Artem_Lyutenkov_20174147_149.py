k = int(input())
c = 0
v = 0
for a in reversed(sorted((int(x) for x in input().split()))):
    if c >= k:
        break
    c += a
    v += 1
print(v if c >= k else -1)