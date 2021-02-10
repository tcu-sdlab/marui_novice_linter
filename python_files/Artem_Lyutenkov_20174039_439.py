R = lambda:map(int, input().split())
n, d = R()
t = list(R())
if sum(t) + 10 * (n - 1) > d:
  print(-1)
else:
  print((d - sum(t)) // 5)