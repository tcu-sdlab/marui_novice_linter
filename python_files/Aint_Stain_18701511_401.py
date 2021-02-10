n,x=map(int,input().split())
a=list(map(int,input().split()))
sum1=abs(sum (a))
s=int(sum1/x)
if sum1%x!=0:
    print(s+1)
else:
    print(s)