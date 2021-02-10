s = input().split(" ")
a = int(s[0])
b = int(s[1])
c = b
d = int(0)
k = int(1)
i = int()
m = [b] * 1
while (d == 0) and (c>a):
    if ((c % 10) == 1):
        c = c // 10
        m.append(c)
        k=k+1
    elif ((c % 2) == 1):
        d = 1
    else:
        c = c//2
        m.append(c)
        k=k+1
if (c==a):
    m = m[::-1]
    print('YES')
    print(k)
    for i in range(0,len(m),1):
        print(m[i],end = ' ')
else:
    print('NO')