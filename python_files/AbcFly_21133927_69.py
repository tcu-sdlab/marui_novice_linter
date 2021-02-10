xl = []
yl = []
zl = []
for i in range(int(input())):
    x,y,z = map(int, input().split())
    xl.append(x)
    yl.append(y)
    zl.append(z)
if sum(xl)==0 and sum(yl)==0 and sum(zl)==0:
    print("YES")
else:
    print("NO")