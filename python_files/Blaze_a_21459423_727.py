n,k=map(int, input().split())
c=[]
count=0
while(k>=n):
    if(n==k):
        c.append(k)
        break
    if(k%2==0):
        c.append(k)
        k=k//2
        
        # count+=1
    else:
        c.append(k)
        if((k-1)%10==0):
            k=(k-1)//10
        else:
            break
        
        # count+=1
if(n==k):
    print("YES")
    print(len(c))
    c=c[::-1]
    # string=""
    # print("{0}".format(" ".join(c)))
    print(*c, sep=' ')
    # print(c[::-1])
else:
    print("NO")