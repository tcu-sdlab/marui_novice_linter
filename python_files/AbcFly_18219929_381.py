m = int(input())
ml = list(map(int,input().split()))
ml.sort()
sl = [ml[0]]
if len(ml)>1:
    fl = [ml[1]]
    for i in range(2,m):
        if sl[len(sl)-1]<ml[i]:
            sl.append(ml[i])
        elif fl[len(fl)-1]<ml[i]:
            fl.append(ml[i])
    if sl[len(sl)-1]==fl[len(fl)-1]:
        fl.pop()
    fl.reverse()
    sl+=fl
print(len(sl))
for i in sl:
    print(i,end=" ")