n,m,a = [int(i) for i in input().split()]
tmp1=n//a
if a*tmp1==n:
    res1=tmp1
else:
    res1=tmp1+1
tmp2=m//a
if a*tmp2==m:
    res2=tmp2
else:
    res2=tmp2+1
print(res1*res2)