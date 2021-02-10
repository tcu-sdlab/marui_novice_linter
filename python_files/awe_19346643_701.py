N, M = map(int, input().split())
B1 = [True for i in range(N)]
B2 = [True for i in range(N)]
S1 = 0
S2 = 0
S = N * N
for i in range(M):
	x, y = map(int, input().split())
	if B1[x - 1]:
		S1 += 1
		B1[x - 1] = False
	if B2[y - 1]:
		S2 += 1
		B2[y - 1] = False
	print(S - (S1 + S2) * N + S1 * S2)