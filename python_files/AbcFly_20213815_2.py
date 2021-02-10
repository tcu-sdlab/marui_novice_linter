n = int(input())
al = []
for i in range(n):
    al+=[input().split()]
r = {}
b = []
for i in range(n):
    x,y = al[i]
    y = int(y)
    if x in r.keys():
        r[x] += y 
    else:
        r[x] = y 
    b+=[[x, r[x]]]
m = max(r.values())
for x,p in b:
    if p>=m and r[x]==m:
        print(x)
        break