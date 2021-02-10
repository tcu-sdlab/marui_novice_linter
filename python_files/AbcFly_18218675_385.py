n, c = map(int, input().split())
p = list(map(int, input().split()))
ls = []
for i in range(n-1):
    ls.append(p[i] - p[i+1] - c)
ls.append(0)
print(max(ls))