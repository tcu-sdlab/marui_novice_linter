a, b = map(int, input().split())
s = [b]
while b > a:
    if b % 2 != 0 and (b - 1) % 10 != 0:
        b = a - 1
    elif b % 2 == 0:
        s += [b // 2]
        b = b // 2
    elif (b - 1) % 10 == 0:
        s += [(b - 1) // 10]
        b = (b - 1) // 10
if b == a:
    print('YES')
    print(len(s))
    for i in range(len(s)):
        print(s[len(s) - i - 1], end=' ')
else:
    print('NO')