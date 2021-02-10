a,b = map(int, input().split())
c = []
found = False
while True:
    c.append(b)
    if b == a:
        found = True
        break
    if b < a:
        break
    if b % 10 == 1:
        b = b // 10
    elif b % 2 == 0:
        b = b // 2
    else:
        break
if not found:
    print('NO')
else:
    print('YES')
    print(str(len(c)))
    st = ' '.join(list(map(str, c[::-1])))
    print(st)