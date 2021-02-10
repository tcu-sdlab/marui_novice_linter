n=int(input())
a=[int(x) for x in input().split()]
ans=0
for i in range(n):
    for j in range(n):
        a[i],a[j]=a[j],a[i]
        for k in range(n):
            if a[k]==n:
                r=k
            if a[k]==1:
                l=k
        ans=max(ans,abs(r-l))
        a[i],a[j]=a[j],a[i]
print(ans)