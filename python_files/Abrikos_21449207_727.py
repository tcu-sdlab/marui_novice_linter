a, b = map(int, input().split())

L = [b]

bl = -50
while b > a:
    if b%10 == 1:
        b //= 10
        L.append(b)
    elif b%2 == 0:
        b //= 2
        L.append(b)
    if bl == b:
        break
    bl = b
    if b == a:
        print('YES')
        print(len(L))
        print(*reversed(L))
        exit()
print('NO')