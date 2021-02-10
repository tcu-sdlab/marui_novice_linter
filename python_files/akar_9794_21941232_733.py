n = int(input())
L = []
sum_l = 0
sum_r = 0
for i in range(n):
    l, r = map(int, input().split())
    L.append((l, r))
    sum_l += l
    sum_r += r
krasa = abs(sum_l - sum_r)
ans = 0
for i in range(n):
    if abs((sum_l - L[i][0] + L[i][1]) - (sum_r - L[i][1] + L[i][0])) > krasa:
        krasa = abs((sum_l - L[i][0] + L[i][1]) - (sum_r - L[i][1] + L[i][0]))
        ans = i + 1
print(ans)