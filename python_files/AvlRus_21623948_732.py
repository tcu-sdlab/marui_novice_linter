q=list(input().split(' '))
n=int(q[0])
k=int(q[1])
b=0
a=list(input().split(' '))
a=[int(a[i]) for i in range(len(a))]
for i in range(len(a)-1):
    c=a[i]+a[i+1]
    if c<k:
        a[i+1]+=(k-c)
        b+=(k-c)
print(b)
for i in range(len(a)):print(a[i],end=' ')