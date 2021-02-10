n = int(input());
a,b= 0,0;
dl = list(map(int, input().split()));
for i in range(n):
    if dl[i]%2==0:
        a+=1;
        ai=i;
    else:
        b+=1;
        bi=i;
    if (a>1 and b==1) or (a==1 and b>1):
        print([ai+1,bi+1][a>b]);
        break;