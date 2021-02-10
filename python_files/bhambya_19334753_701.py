n = int(input())
a = list(map(int, input().split()))


x = (sum(a) * 2) // n

b = [False for i in range(n)]
for i in range(n):
	if not b[i]:
		for j in range(i + 1, n):
			if not b[j]:
				if a[i] + a[j] == x:
					print(i + 1, j + 1)
					b[i] = True
					b[j] = True
					break