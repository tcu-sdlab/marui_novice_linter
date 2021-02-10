n,m,k = [int(x) for x in input().split(' ')]
rows = [[0,-1]]*n
cols = [[0, -1]]*m
for i in range(k):
    tmp = [int(x) for x in input().split(' ')]
    if tmp[0] == 1:
        rows[tmp[1]-1] = [tmp[2], i]
    else:
        cols[tmp[1]-1] = [tmp[2], i]

for i in range(n):
    for j in range(m):
        print(rows[i][0] if rows[i][1] > cols[j][1] else cols[j][0], end = ' ')
    print()