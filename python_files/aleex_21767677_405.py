n = int(input())
a = [0] * n
a = list(map(int, input().split()))
a.sort()
for i in range(n) :
    print(a[i], end = " ")