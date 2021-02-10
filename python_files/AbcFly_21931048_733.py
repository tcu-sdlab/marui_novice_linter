n = int(input());
dl  = [];
ans = L = R = 0;
for i in range(n):
    l,r = map(int, input().split());
    L+=l;
    R+=r;
    dl+=[[l,r]];
ans = abs(L-R);
index=-1
for i in range(n):
    ts=abs(L-R+2*(-dl[i][0]+dl[i][1]));
    if ts>ans:
        ans=ts;
        index=i;

print(index+1);