from math import sqrt
from decimal import Decimal

t = input
p = print
r = range

a, b = map(int, t().split())
n = int(t())
ans = float('inf')

for i in range(n):
    x, y, v = map(int, t().split())
    dist = (Decimal(sqrt((x - a) ** 2 + (y - b) ** 2))) / v
    ans = min(ans, dist)
p("%.20f" % Decimal(ans))