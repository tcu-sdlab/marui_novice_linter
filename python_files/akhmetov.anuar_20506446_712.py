t = input
p = print
r = range
n = int(t())
a = list(map(int, t().split()))
b = [0] * n
for i in range(n - 1):
    b[i] = a[i] + a[i + 1]
b[n - 1] = a[n - 1]
print(' '.join(map(str, b)))