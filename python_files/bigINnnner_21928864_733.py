c = [(0, 0)] + [list(map(int, input().split())) for _ in range(int(input()))]
d = list(zip(*c))
L = sum(d[0])
R = sum(d[1])
ans = [abs(L - R - (x[0] - x[1]) * 2) for i, x in enumerate(c, 1)]
print(ans.index(max(ans)))