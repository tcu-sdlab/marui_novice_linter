n = int(input())
mt = [[0 for col in range(n)] for row in range(n)]
r = 0
c = (n - 1) // 2
x = 1
# print(mt)
while x < n * n + 1:
    mt[r][c] = x
    # print(mt)
    if not x % n:
        r = (r + 1) % n
    else:
        r = (r - 1 + n) % n
        c = (c + 1) % n
    x += 1
# print(mt)
for i in range(n):
    for j in range(n):
        print("%s%d" % (" " if j else "", mt[i][j]), end="")
    print()