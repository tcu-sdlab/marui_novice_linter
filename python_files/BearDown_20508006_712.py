S = input()
l = 0
r = 0
u = 0
d = 0
if len(S)%2!=0:
    print(-1)
else:
    for i in S:
        if i=='L':
            l+=1
        elif i=='R':
            r+=1
        elif i=='U':
            u+=1
        else:
            d+=1
    lr = abs(l-r)
    ud = abs(u-d)
    print(int((lr+ud)/2))