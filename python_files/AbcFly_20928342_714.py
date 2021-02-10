input()
al = list(map(int, input().split()))
ans = 0
amin = min(al)
amax = max(al)
sa = set(al)
if len(sa)<3:
    ans=1
elif (amin+amax)%2==0:
    sa = set(al)
    sa.remove(amin)
    sa.remove(amax)
    sa.add((amin+amax)//2)
    if len(sa)==1:
        ans=1
print(["NO","YES"][ans])