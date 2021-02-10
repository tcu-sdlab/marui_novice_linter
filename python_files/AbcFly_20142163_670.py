n,k = map(int,input().split())
dl = list(map(int, input().split()))
n=int(k**(0.5))-1
while n*(n+1)<=2*k:
    n+=1
n-=1
m = k-n*(n+1)//2
if m>0:
    n=m
print(dl[n-1])