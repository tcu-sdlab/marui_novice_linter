n,d=map(int,input().split())
r=0
c=0

for i in range(d):
    if '0' in input():
        c+=1
    else:
        c=0
    r= max(r,c)


print(r)