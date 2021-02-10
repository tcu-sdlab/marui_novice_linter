bus=["" for i in range(1010)]
ans="NO"
loop=True
n = int (input().strip())
for i in range(n):
    inp=input().strip()
    if(loop and (inp[0]=='O' and inp[1]=='O') ):
        ans="YES"
        loop=False
        bus[i]= "++|"+inp[3]+inp[4]
    elif(loop and  inp[3]=='O' and inp[4]=='O'):
        ans="YES"
        loop=False
        bus[i]= ""+inp[0]+inp[1]+"|++"
    else:
        bus[i]=inp
print(ans)
if(not loop):
    for i in range(n):
        print(bus[i])