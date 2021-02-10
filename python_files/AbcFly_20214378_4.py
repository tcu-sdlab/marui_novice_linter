d, sumTime = map(int, input().split())
minl = []
maxl = []
for i in range(d):
    a, b = map(int, input().split())
    minl+=[a]
    maxl+=[b]
if sum(minl)<=sumTime<=sum(maxl):
    print("YES")
    sumTime-=sum(minl)
    for i in range(d):                                                                                                                                          
        print(minl[i]+min(sumTime, maxl[i]-minl[i]))
        sumTime = max(0, sumTime-maxl[i]+minl[i])
else:
    print("NO")