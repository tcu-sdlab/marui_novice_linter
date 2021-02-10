n, k = map(int, input().split())
table = [len(input()) for _ in range(n)]
x = len(input())
a = len(list(filter(lambda s: s < x, table)))
b = len(list(filter(lambda s: s <= x, table)))
print(a // k * 5 + a + 1, (b - 1) // k * 5 + b)