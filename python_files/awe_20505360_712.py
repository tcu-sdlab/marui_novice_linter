n = int(input())
a = list(map(int, input().split()))
for i in range(n - 1):
	print(a[i] + a[i + 1], end=' ')
print(a[n - 1], end='')