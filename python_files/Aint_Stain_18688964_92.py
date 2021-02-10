a,b=list(map(int,input().split()))
c=int((a*(a+1))/2)
d=int(b%c)
e=1
while d>=e:
    d-=e
    e+=1

print(d)