n = int(input())
a = list(map(int, input().split()))
c = 0
s = 0
b = 0
for i in range(n):
    if a[i] == 0:
        s, c = 0, 0
    if a[i] == 1:
        if c == 0:
            c = 1
            s = 0
            b += 1
        else:
            c = 0
            s = 0
    if a[i] == 2:
        if s == 0:
            c = 0
            s = 1
            b += 1
        else:
            c = 0
            s = 0
    if a[i] == 3:
        if s + c == 0:
            b += 1
        if s == 1:
            c = 1
            s = 0
            b += 1
            continue
        if c == 1:
            c = 0
            s = 1
            b += 1
            continue

print(n - b)