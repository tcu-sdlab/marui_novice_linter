n = int(input())
L = []
for i in range(n):
    a, b, c = sorted(map(int, input().split()))
    L.append((c, b, a, i + 1))
L.sort()
ans_1 = 0
ans_21 = 0
ans_22 = 0
res = 0
f = False
for i in range(1, n):
    if L[i][2] > L[ans_1][2]:
        ans_1 = i
    if L[i][0] == L[i - 1][0] and not f:
        ans_21 = i - 1
        ans_22 = i
        res = min(L[ans_21][0], L[ans_21][1], L[ans_21][2] + L[ans_22][2])
        f = True
    elif L[i][0] == L[i - 1][0] and L[i][1] == L[i - 1][1]:
        if res < min(L[i][0], L[i][1], L[i][2] + L[i - 1][2]):
            ans_21 = i - 1
            ans_22 = i
            res = min(L[i][0], L[i][1], L[i][2] + L[i - 1][2])
if L[ans_1][2] >= res:
    print(1)
    print(L[ans_1][3])
else:
    print(2)
    print(L[ans_21][3], L[ans_22][3])          
#print(L)