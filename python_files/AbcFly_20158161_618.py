n = int(input())
s=[]
for i in range(20,-1,-1):
    if n&(1<<i) >0:
        s+=[str(i+1)]
print(" ".join(s))