# contest/733/problem/B

n = int(input())
LR = [list(map(int, input().split())) for _ in range(n)]

suml = sum( (LR[i][0] for i in range(n)) )
sumr = sum( (LR[i][1] for i in range(n)) )

sgn = lambda x: x//abs(x) if x != 0 else 0

resb = [abs(suml - sumr + 2 * (LR[i][1]-LR[i][0])) for i in range(n)]
maxind = 0
for i in range(1, n):
    if resb[maxind] < resb[i]:
        maxind = i

print(maxind+1 if resb[maxind] > abs(suml-sumr) else 0)