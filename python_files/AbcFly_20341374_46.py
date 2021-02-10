n = int(input())
pl = list(range(1,n+1))
cnt = 1
cindex = 1
ans = []
while cnt<n:
    j=1
    while j<cnt:
#         if pl[cindex]>0:
        j+=1
        cindex=(cindex+1)%n
    ans+=[str(pl[cindex])]
#     pl[cindex]=0
    cindex=(cindex+1)%n
    cnt+=1
print(" ".join(ans))