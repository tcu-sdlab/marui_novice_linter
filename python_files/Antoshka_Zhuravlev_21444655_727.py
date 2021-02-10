a,b = map(int,input().split())
v = b
c = []
k = 0
while a < b:
    z = len(str(b))
    if str(b)[z-1] == '1':
        b = int((b - 1)/10)
        c.append(b)
        k += 1
    elif b % 2 == 0:
        b = int(b/2)
        c.append(b)
        k += 1
    else:
        break
if a != b:
    print('NO')
else:
    print('YES')
    print(k+1)
    if len(c) == k:
        c = c[::-1]
        for x in c:
            print(x, end = ' ')
        print(v)