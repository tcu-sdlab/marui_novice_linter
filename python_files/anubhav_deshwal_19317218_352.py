in1=input()
in2=input()
ls=in2.split()
c5=ls.count('5')
c0=ls.count('0')
d = int(c5/9)
i=0
l=[]
flag=0
if c0 == 0:
    print(-1)
else:
    if d == 0:
        flag=1
    while i < (d*9):
        l.append(5)
        i+=1
    if flag == 1:
        print(0)
    else:
        i=0
        while i < c0:
            l.append(0)
            i+=1
        b = int(''.join(map(str, l)))
        print(b)