n, m = list(map(int, input().split(' ')))
rowset = set()
colset = set()
ans = []
for i in range(m):
    a, b = [int(x) for x in input().split(' ')]
    rowset.add(a)
    colset.add(b)
    ans.append((n-len(rowset))*(n-len(colset)))

print(' '.join(map(str, ans)))