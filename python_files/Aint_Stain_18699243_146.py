n=int(input())
s=int(n/2)
a=list(map(int,input()))
#a=[int(x) for x in input()]
if a.count(4)+a.count(7)==n and sum(a[:s])==sum(a[s:]):
    print("YES")
else:
    print("NO")