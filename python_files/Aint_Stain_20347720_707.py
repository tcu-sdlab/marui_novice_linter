n=int(input())
if(n<3):
    print(-1)
    exit()
if n%2==1:
    x=(n*n-1)//2
    y=(n*n+1)//2
else:
    x=(n//2)**2-1
    y=x+2
print(x,y)