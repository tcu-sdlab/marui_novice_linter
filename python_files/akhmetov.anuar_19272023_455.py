t = input
p = print
r = range
n = int(t())
a = [0] * 100002
for i in map(int, t().split()):
    a[i] += 1
f = [0, a[1]]
for i in range(2, 100002):
    f.append(max(f[i - 1], f[i - 2] + a[i] * i))
print(f[100001])