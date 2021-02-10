n=int(input().strip())
inp=input().strip().split()
p=[int(i) for i in inp]

t=True
ans="YES"
for i in range(n):
    inp= input().strip()
    if(not t):
        continue
    v=0
    for x in inp:
        if( (x=='a')or(x=='e')or(x=='i')or(x=='o')or(x=='u')or(x=='y') ):
            v+=1
    if(v!= p[i] ):
        ans="NO"
        t=False
print(ans)