inp = input().strip().split(" ")
n,m= int(inp[0]), int(inp[1] )

flag= 0

for i in range(n):
    inp= input().strip().split(" ")
    if(flag==0):
        for x in inp:
            if( x=='C' or x=='M' or x=='Y' ):
                flag=1
                break

if(flag==0):
    print("#Black&White")
else:
    print("#Color")