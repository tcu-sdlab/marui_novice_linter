import math
n = int(input())
a = list(map(int, input().split()))
b = [[a[i], i + 1] for i in range(n)]

b.sort()

for i in range(0, n // 2):
    print("%d %d"%(b[i][1], b[n - i - 1][1]))