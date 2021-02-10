n,k = map(int, input().split())
la=[]
for i in range(100):
    la.append(0)
for i in range(n):
    x=input()
    a=len(x)
    la[a-1]+=1
q=0
z=input()
al=len(z)

for i in range(100):
    if(i<al-1):
        q+=la[i]
    if(i==al-1):
        break

t=q
extra=q//k
t=t+(extra*5)
q=q%k
best=t+1
t+=la[al-1]-1
q+=la[al-1]-1
extra=q//k
t+=(extra*5)
t+=1
worst=t
print(str(best)+' '+str(worst))