# cook your dish here
n,m=map(int,input().split())
a=list(map(int,input().split()))
l=len(a)
c=0
s=0
i=0
while i<l:
    s=a[i]
    c+=1
    while s<=m:
        i+=1
        if i<l:
            s+=a[i]
        else:
            break
        
print(c)