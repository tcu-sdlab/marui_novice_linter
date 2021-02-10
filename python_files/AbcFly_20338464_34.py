n, m = map(int, input().split())
ts = list(map(int, input().split()))
ans=0
ts.sort()
i = 0
while i<m and ts[i]<0:
    ans-=ts[i]
    i+=1
print(ans)