s=input()
dg=[]
n='';z=0
for i in range(len(s)):
    if s[i].isdigit() or s[i]=='.':
        n+=s[i]
        z=1
    elif z:dg.append(n);n='';z=0
dg.append(n)
sm=0
for i in range(len(dg)):
    x=(dg[i].split('.'))
    io=''
    if len(x)>2 or len(x[len(x)-1])==3:
        for j in range(len(x)):
            if len(x[j])==3 or j==0:io+=x[j]
            else:io=io+'.'+x[j]
        sm=round(sm+float(io),2)
    else:sm=round(sm+float(dg[i]),2)
sm=str(sm)
b=sm.split('.');
for i in range(len(b[0])):
    print(int(b[0][i]),end='')
    if len(b[0][i+1:])%3==0 and len(b[0][i+1:])!=0:print('.',end='')
if len(b[1])==2 and b[1]!='00' and  b[1]!='0':print('.',b[1],sep='')
elif b[1]!='00' and  b[1]!='0':print('.',b[1],0,sep='')