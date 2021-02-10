n=int (input())
st=input()
l=len(st)
k=0
kl=[]
f=0
for i in range(0,l):
    if(st[i]=='B'):
        f+=1
    elif(f!=0):
        kl.append(f)
        f=0
        k+=1
if f!=0:
    k+=1
    kl.append(f)

print(k)
for _ in kl:
    print(_,end=' ')