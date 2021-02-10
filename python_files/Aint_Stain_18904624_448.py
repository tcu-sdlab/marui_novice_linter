a=sum(map(int,input().split()))
b=sum(map(int,input().split()))
n=int(input())
if ((a+4)//5+(b+9)//10)<=n:
    print("YES")
else:
    print("NO")