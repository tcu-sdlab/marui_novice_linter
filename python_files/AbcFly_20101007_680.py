n,a = map(int, input().split())
tl = list(map(int, input().split()))
l=a-2
r=a
res=tl[a-1]
while l>=0 or r<n:
    if l>=0 and r<n and tl[l]==tl[r]==1:
        res+=2
    elif (l<0 and tl[r]==1) or (r>=n and tl[l]==1):
        res+=1
    l-=1
    r+=1
print(res)