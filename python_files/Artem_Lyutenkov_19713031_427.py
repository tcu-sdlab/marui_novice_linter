n, p, d = int(input()), 0, 0
for i in (int(x) for x in input().split()):
    p += i
    if p == -1:
        p = 0
        d += 1
print(d)