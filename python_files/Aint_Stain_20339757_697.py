a,b,c=list(map(int,input().split()))
if (a==c):
    print("YES")
elif c>=a+b and ((c-a)%b==1 or (c-a)%b==0):
    print("YES")
else:
    print("NO")