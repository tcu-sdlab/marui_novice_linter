def ind(N, el, B, A):
	for i in range(N):
		if B[i]:
			if A[i] == el:
				return i
	return 0			
N = int(input())
A = list(map(int, input().split()))
B = [True for i in range(N)]
summ = (sum(A) * 2) // N
for i in range(N):
	if B[i]:
		B[i] = False
		x = ind(N, summ - A[i], B, A)
		B[x] = False
		print(i + 1, x + 1)