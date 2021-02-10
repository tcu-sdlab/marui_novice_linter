a = list(map(int, input().split()))
a.sort()

dist = (a[1] - a[0]) + (a[2]-a[1])
print(dist)