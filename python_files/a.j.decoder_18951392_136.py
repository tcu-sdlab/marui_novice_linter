n=int(input())
r=list(range(n))
b=list(map(int,input().split()))
for m in range(n):
    r[b[m]-1]=m+1
for i in r:
    print(i,end=' ')