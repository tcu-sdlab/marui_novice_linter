n,k = map(int, input().split())
m = n%k
if m==0:
    m=k
else:
    m=k-m
print(n+m)