n, m = map(int, input().split());
l = [input() for i in range(n)];
i1, i2, j1, j2 = n - 1, 0, m - 1, 0;
for i in range(n):
    if (l[i].find('*') != -1):
        i1, i2, j1, j2 = min(i1, i), max(i2, i), min(j1, l[i].find('*')), max(j2, l[i].rfind('*'))
for i in range(i1, i2 + 1):
    print(l[i][j1:j2 + 1]);