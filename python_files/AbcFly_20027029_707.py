n,m = map(int,input().split())
color = set("CMY")
cs = set()
for i in range(n):
    cs=cs.union(set(input().split()))
if len(cs.intersection(color))==0:
    print("#Black&White")
else:
    print("#Color")