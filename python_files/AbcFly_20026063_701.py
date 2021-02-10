n,m = map(int,input().split())
c,r,ans = set(),set(),[]
for i in range(m):
    x,y = map(int, input().split())
    c.add(x)
    r.add(y)
    ans+=[str((n-len(c))*(n-len(r)))]
print(" ".join(ans))