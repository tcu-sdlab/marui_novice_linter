l,r = 0, 0
for s in input():
    if s=='(':
        l+=1
    elif l>0:
        r+=1
        l-=1
print(2*r)