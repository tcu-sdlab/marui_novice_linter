n,m=list(map(int,input().split()))
ara=list(map(int,input().split()))
k=0
for i in range(1,m):
    if ara[i - 1]>ara[i]:
        k+=1
print(ara[m-1]+((n*k))-1)