a=input()+" "
q=""
p=[]
for i in range(len(a)):
    if a[i]==" ":
        if q!="":   
            p.append(int(q))
        q=""
    else:
        q=q+a[i]
d=input()+" "
l=[]
q=""
for i in range(len(d)):
    if d[i]==" ":
        l.append(int(q))
        q=""
    else:
        q=q+d[i]
w=1
for i in range(1,len(l)):
    if l[i]-l[i-1]>p[1]:
        w=1
    else:
        w+=1
print(w)