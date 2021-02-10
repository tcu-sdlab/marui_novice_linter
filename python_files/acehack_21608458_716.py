n, c = map(int, input().split())
cnt = 0
pt = 0
for t in map(int, input().split()):
    if t - pt <= c:
        cnt += 1
    else:
        cnt = 1
    pt = t

print(cnt)