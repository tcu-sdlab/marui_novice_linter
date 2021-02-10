n, m = map(int, input().split())

t= 1001

p = sorted(list(map(int, input().split())))

for i in range(m-n+1):
    t = min(abs(p[i]-p[i+n-1]), t)

print(t)