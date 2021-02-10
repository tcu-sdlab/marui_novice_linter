n, m = map(int, input().split())
a = [[int(x) for x in input().split()] for _ in range(m)]
c = [0] * n
for x in a:
    c[x.index(max(x))] += 1
print(c.index(max(c)) + 1)