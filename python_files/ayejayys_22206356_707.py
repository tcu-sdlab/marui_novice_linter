n, m,k = [int(x) for x in input().split(' ')]
pairs = []
for i in range(m):
    pairs.append(list(map(int, input().split(' '))))
if not k:
    print(-1)
else:
    store = set(map(int, input().split(' ')))
    ans = 10**9+5
    for i in pairs:
        a = i[0] in store
        b = i[1] in store
        if (a and not b) or (not a and b):
            ans = min(ans, i[2])
    print(-1 if ans == 10**9+5 else ans)