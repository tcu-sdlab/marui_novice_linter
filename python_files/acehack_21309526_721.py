n, k = map(int, input().split())
xs = []
for i in range(0, n):
    xs.append(input())

lp = len(input())

xs.sort(key=lambda s: len(s))

best = 0
worst = 0
t = 1
for i in xs:
    if len(i) < lp:
        best += 1
        if (t % k) == 0:
            best += 5
        t += 1
    else:
        best += 1
        break

t = 1
for i in xs:
    if not len(i) > lp:
        if ((t-1) % k) == 0 and t != 1:
            worst += 5
        worst += 1
        t += 1
    else:
        break

print(best, worst)