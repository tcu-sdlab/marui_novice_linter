l=list(map(int,input().split()))
n=0
b=l[0]
d=l[1]
s=l[2]
l.sort(reverse=True)
b-=l[0]
d-=l[0]
s-=l[0]
k1=l[0]
k2=l[1]
k3=l[2]
if k1>k2+1:
    n=n+(k1-(k2+1))
if k1>k3+1:
    n=n+(k1-(k3+1))
print(n)