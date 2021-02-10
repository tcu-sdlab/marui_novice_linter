n = int(input())
xs = input()
r1, r2, b1, b2 = 0, 0, 0, 0

for i, c in enumerate(xs):
    if (i % 2) == 0:
        if c == 'r': r1 += 1
        else: b2 += 1
    else:
        if c == 'r': r2 += 1
        else: b1 += 1

print(min(max(r1, b1), max(r2, b2)))