t = input
p = print
r = range
k, R = map(int, t().split())
reminder = k % 10
ans = 1
while reminder != 0:
    if reminder == R:
        break
    reminder += (k % 10)
    reminder %= 10
    ans += 1
p(ans)