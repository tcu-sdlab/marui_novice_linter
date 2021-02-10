n=int(input())
a=list(input().split(' '))
a=[ int(a[i]) for i in range(len(a))]
for i in range(len(a)):
   if a[i]>=2:a[i]-=int(a[i]//2)*2
   if i!=len(a)-1 and a[i]==1:
        a[i]-=1
        a[i+1]-=1
   if a[i]!=0:print('NO');break
else:print('YES')