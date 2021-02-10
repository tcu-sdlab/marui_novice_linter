p,q=list(map(int,input().split()))
n=int(input())
ara= list(map(int,input().split()))
b=0
a=1
l=0
for i in ara[::-1]:
    l=a
    a=(i*a)+b
    b=l
#print(a*q,b*p)
if a*q==b*p:
    print("YES")
else:
    print("NO")