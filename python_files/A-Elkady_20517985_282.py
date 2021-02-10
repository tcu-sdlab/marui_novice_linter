n=int(input())
x=0;y=0
for i in range(n):
    a= input()  
    if '++' in a: x=x+1
    else : y=y-1      
if x>y:print(x+y)
#else: print(y-x)