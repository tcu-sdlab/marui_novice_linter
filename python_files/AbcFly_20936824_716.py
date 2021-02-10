n,c = map(int,input().split())
tl = list(map(int, input().split()))
tl.insert(0, 0)
ans = 0
for i in range(n):
    sub = tl[i+1]-tl[i]
    if sub<=c:
        ans+=1
    else:
        ans=1
print(ans)