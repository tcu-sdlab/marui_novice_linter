a,b=map(int,input().split())

c=str
d=0
h=[]
h.append(b)
while b>a:
    if b%2==0:
        b=b//2
        h.append(b)
    elif b%10==1: #if str(b)[len(str(b))-1:]=='1'
        b=b//10
        h.append(b)
    else:
        break

h.reverse()
if a==b:
    print("YES")
    print(len(h))
    for i in range (len(h)):
        print(h[i],end=" ")
else:
    print("NO")