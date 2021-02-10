l,r,k = map(int,input().split())
ki=1
ok = 0
while(ki<=r):
    if(ki>=l and ki<=r):
        print(ki,end=" ")
        ok = 1
    ki=ki*k

if(ok==0):
    print("-1")