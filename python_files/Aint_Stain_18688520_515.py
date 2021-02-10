a,b,s=list(map(int,input().split()))
r=s-(abs(a)+abs(b))
if r==0 or (r%2==0 and r>0):
    print("Yes")
else:
    print ("No")