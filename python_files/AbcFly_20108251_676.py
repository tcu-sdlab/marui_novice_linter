n=int(input())
al = list(map(int, input().split()))
a,b = al.index(min(al)), al.index(max(al))
if a>b:
    a,b = b,a
if n>3:
    if a-0>n-1-b:
        a=0
    else:
        b=n-1
elif n==3:
    a=0
    b=2  
print(b-a)