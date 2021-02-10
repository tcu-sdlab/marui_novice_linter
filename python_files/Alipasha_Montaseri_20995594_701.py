n=int(input())
l=(input().split())
for i in range(len(l)):
    l[i]=int(l[i])


for j in range(n//2):
    indexerk=0
    indexerb=0
    k=120
    b=0
    for i in range(len(l)):
        if l[i]<k and l[i]!=-1:
            k=l[i]
            indexerk=i
        if l[i]>=b and l[i]!=-1:
            b=l[i]
            indexerb=i
    
    print(indexerk+1,indexerb+1)
    l[indexerk]=-1
    l[indexerb]=-1