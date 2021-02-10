(n, t), a = map(int, input().split()), list(map(int, input().split()))
x = 0
while x != t - 1 and x != n - 1:
    x += a[x]
print("YES" if x == t - 1 else "NO")