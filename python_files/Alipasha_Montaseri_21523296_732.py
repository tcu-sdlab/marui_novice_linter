l=list(map(int,input().split()))
k=l[0]
r=l[1]
q=0
while True:
    q+=1
    if (k*q)%10==0 or ((k*q)-r)%10==0:
        print(q)
        break