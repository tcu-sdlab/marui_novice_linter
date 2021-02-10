import math

n, m, a = input().split()
n = float(n)
m = float(m)
a = float(a)

print(math.ceil(n / a) * math.ceil(m / a))