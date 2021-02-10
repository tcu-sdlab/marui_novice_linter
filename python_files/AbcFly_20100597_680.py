tl = list(map(int, input().split()))
res = []
for t in tl:
    c = tl.count(t)
    if c==1: c=0
    elif c>3: c=3
    res+=[t*c]
res.sort(reverse=True)
        
print(sum(tl)-res[0])