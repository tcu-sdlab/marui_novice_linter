n=int(input())
a=1234567
b=123456
c=1234
for i in range(n//a+1):
    for j in range(n//b+1):
        t = n-i*a-j*b
        if t<0:
            break
        elif t%c==0:
            print("YES")
            exit()
print("NO")