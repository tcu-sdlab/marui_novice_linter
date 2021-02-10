n = int(input())
p = list(map(int, input().split()))
a = set('auiyoe')
log = True
for i in range(n):
    s = input()
    cnt = 0
    for el in s:
        if el in a:
            cnt += 1
    if cnt != p[i]:
        log = False
if log:
    print('YES')
else:
    print('NO')