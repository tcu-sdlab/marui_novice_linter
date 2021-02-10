n, m = map(int, input().split())
ans = n // m
A = list(map(int, input().split()))
B = [0 for i in range(m)]
for i in A:
	if i <= m:
		B[i - 1] += 1
ost = n - m * ans
change = 0
for i in range(m):
	if B[i] < ans:
		change += ans - B[i]
print(ans, change)
b = True
ind = 0
for i in A:
	if b and (i > m or B[i - 1] > ans):
		while b and B[ind] >= ans:
			ind += 1
			if ind >= m:
				b = False
				print(i, end=' ')
		if b:
			B[ind] += 1
			if i <= m:
				B[i - 1] -= 1
			print(ind + 1, end =' ')
	else:
		print(i, end=' ')