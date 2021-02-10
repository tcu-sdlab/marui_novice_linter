n,t=map(int,input().split())
a=list(map(int,input().split()))
x=int(1)
while x<t:
    x=x+a[x-1]
if x==t:
    print("YES")
else:
    print("NO")