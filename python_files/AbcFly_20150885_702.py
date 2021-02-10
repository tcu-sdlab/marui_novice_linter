n = int(input())
al = list(map(int, input().split()))+[0]
res=[]
s=0
for i in range(1,n+1):
    if al[i]<=al[i-1]:
        res+=[i-s]
        s=i
print(max(res))