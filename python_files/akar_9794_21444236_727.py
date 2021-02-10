a, b = map(int, input().split())
L = [b]
while a < b:
    if b % 2 == 0:
        b //= 2
        L.append(b)
    elif b % 10 == 1:
        b //= 10
        L.append(b)
    else:
        break
if a == b:
    print('YES')
    print(len(L))
    L.reverse()
    print(*L)
else:
    print('NO')