n=int(input())
s=list(map(int,input().split()))
mx=s.index(max(s));minm=10000000;x=0
for i in range(n):
        if minm>=s[i]:
                minm=s[i]
                x=i
if mx>x:
        print(mx+(n-1)-x-1)
else:
        print(mx+(n-1)-x)