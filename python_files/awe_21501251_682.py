n, m = map(int, input().split())
A = [n // 5 for i in range(5)]
B = [m // 5 for i in range(5)]
for i in range(5):
	if n % 5 > i:
		A[i] += 1
for i in range(5):
	if m % 5 > i:
		B[i] += 1
print(A[0] * B[3] + A[1] * B[2] + A[2] * B[1] + A[3] * B[0] + A[4] * B[4])