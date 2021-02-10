n,k,t = map(int, input().split())
sum = (n*k*t//100)
a,b = sum//k, sum%k 
ans=[0]*n
ans[0:a]=[k]*a
if b>0:
    ans[a]=b
for t in ans:
    print(t,end=" ")