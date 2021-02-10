n = int(input())
xl = list(map(int, input().split()))
xl.sort()
xl+=[xl[n-1]+1]

q = int(input())
ml = []
for i in range(q):
    x=int(input())
    if xl[n]<=x:
        x=xl[n-1]
    ml+=[x]
    
xl.sort()
xl+=[xl[n-1]+1]
res = []
index = 0
for i in range(xl[n]):
    while i >= xl[index]:
        index+=1
    res+=[index]
# print(res)   
# print(ml) 
for i in range(q):
    print("%d" % res[ml[i]])