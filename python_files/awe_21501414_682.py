n = int(input())
A = list(map(int, input().split()))
A.sort()
c = 0
for i in range(n):
	if A[i] + c < i + 1:
		c += 1
print(n + 1 - c)