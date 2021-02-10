read = lambda: map(int,input().split())
n, a = read()
x = sorted(read())
result = 0
if n > 1:
    r1 = abs(a - x[0]) + abs(x[0] - x[n-2])
    r2 = abs(a - x[1]) + abs(x[1] - x[n-1])
    r3 = abs(a - x[n-2]) + abs(x[n-2] - x[0])
    r4 = abs(a - x[n-1]) + abs(x[n-1] - x[1])
    result = min(r1, r2, r3, r4)
print(result)