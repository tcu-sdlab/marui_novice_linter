n = int(input())
a = map(int, input().split())
a = list(a)
a.sort()
print(a[(n - 1) // 2])