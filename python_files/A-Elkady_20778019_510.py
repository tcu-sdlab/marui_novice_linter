n,m=map(int,input().split())
x='.'*(m-1)+'#'
for i in range(n):
        if i%2==0:print('#'*m)
        elif(i%4==1):print(x)
        else:print(x[::-1])