n,m = map(int,input().split())
ln = list(map(int,input().split()))
lm = list(map(int,input().split()))
i=j=0
#难度<= ok
while i<n and j<m:
    if ln[i]<=lm[j]:
        i+=1
    j+=1    
print(n-i)