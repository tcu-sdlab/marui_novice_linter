n,m=map(int,input().split())
sum = 0
for i in range(1000):
    b = n - i**2
    if 0<=b<=1000 and i+b**2==m:
        sum+=1
print(sum)