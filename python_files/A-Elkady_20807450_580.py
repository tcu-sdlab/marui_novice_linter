n=int(input())
m=list(map(int,input().split()))
x=0;count=1
for i in range(n-1):
                if m[i] <= m[i+1]:count+=1
                else: x=max(x,count); count=1
print(max(count,x))