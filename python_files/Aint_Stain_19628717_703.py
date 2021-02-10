a=int(input())
xx=0
yy=0
for i in range(a):
    x,y=map(int,input().split())
    if(x>y):
        xx+=1
    elif(y>x):
        yy+=1
if(xx>yy):
    print("Mishka")
elif(xx<yy):
    print("Chris")
else:
    print("Friendship is magic!^^")