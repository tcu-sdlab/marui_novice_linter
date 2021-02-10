d = list(map(int, input().split()))
ans = 3 * max(d) - sum(d) if max(d) > 1 else 0
for i in range(4):
    for j in range(4):
        dd = [0, 0, 0]
        for k in range(i, 3): 
            if d[k]: 
                dd[k] += 1
        for k in range(j): 
            if d[k] - dd[k]: 
                dd[k] += 1
        m = max([d[k] - dd[k] for k in range(3)])
        ans = min(ans, sum([(i <= k) + (j > k) + m - d[k] for k in range(3)]))
print(ans)