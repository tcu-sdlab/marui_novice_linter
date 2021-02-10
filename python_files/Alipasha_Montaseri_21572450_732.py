l=list(map(int,input().split()))
n=l[0]
k=l[1]
l=list(map(int,input().split()))
o=0
w=[]
for i in range(len(l)):
    w.append(l[i])
if len(l)==1:

    print(0)
    print(l[0])
else:
    for i in range(len(l)):
        if i==0:
            if l[0]+l[1]<k:
                l[1]=l[1]+abs(k-(l[0]+l[1]))
        elif i==len(l)-1:
            if l[i-1]+l[i]<k:
                l[i-1]=l[i-1]+abs(k-(l[i]+l[i-1]))
        else:
            if l[i]+l[i+1]<k:
                l[i+1]=l[i+1]+abs(k-(l[i]+l[i+1]))
    o=0
    for i in l:
        o+=i
    for i in w:
        o-=i

    s=""
    for i in l:
        s=s+str(i)
        s=s+" "
    print(o)
    print(s)