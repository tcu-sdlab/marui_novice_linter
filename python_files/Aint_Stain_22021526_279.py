n,t=map(int,input().split())
ara= [int(x) for x in input().split()]
s=0
count=0
ma=0
for i in range(0,n):
    while t<ara[i]:
        t+=ara[s]
        s+=1
        count-=1
    t-=ara[i]
    count+=1

    if count>=ma:
        ma=count
print(ma)