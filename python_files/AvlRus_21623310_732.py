n=list(input().split(' '))
k=int(n[0])
r=int(n[1])
i=1
while 1 :
    if (k*i)%10==0 or (k*i)%10==r:break
    i+=1
print(i)