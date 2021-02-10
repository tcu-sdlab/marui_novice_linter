m=list(input().split(' '))
a=int(m[0])
b=int(m[1])
n=[]
while b>a :
    n.append(b)
    if b%2==0:b=int(b/2)
    elif b%10==1:b=int(b//10)
    else:break
n.append(a)
if a==b:
    print('YES')
    print(len(n))
    for i in range(1,len(n)+1):
        print(n[len(n)-i],'',end='')
else:print('NO')