n=int(input())
ds = input()
tl = list(map(int,input().split()))
ans=[tl[i+1]-tl[i] for i in range(n-1) if ds[i]=="R" and ds[i+1]=="L"]
if len(ans)>0:
    print(min(ans)//2)
else:
    print(-1)