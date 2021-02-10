n = int(input())
a = list(map(int, input().split()))
b = [[a[y], y + 1] for y in range(n)]
b.sort()
for i in range(n // 2):
        print(str(b[i][1]) + ' ' + str(b[n - i - 1][1]))