t = input
p = print
r = range
n, k = map(int, t().split())
a = list(map(int, t().split()))

ans = sum(a)
for i in r(n - 1):
    if a[i] + a[i + 1] <= k:
        a[i + 1] += (k - a[i + 1] - a[i])
ans = sum(a) - ans
p(ans)
p(" ".join(map(str, a)))