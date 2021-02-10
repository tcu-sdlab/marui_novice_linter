n = int(input())
mylist = []
myset = set()
isOk = True
for i in range(n):
    mystr = input()
    ts = set(mystr)
    if len(ts)==2 and mystr[i]==mystr[-(i+1)] and isOk:
        tlist = list(mystr)
        mylist.append(tlist)
        tlist[i]=' '
        tlist[-(i+1)]=' '
        myset = myset.union(ts)
        ts = set(tlist)
        myset = myset.union(ts)
        if len(ts)!=2 or len(myset)!=3:
            isOk = False
    else:    
        isOk = False
if isOk:
    print("YES")
else:
    print("NO")