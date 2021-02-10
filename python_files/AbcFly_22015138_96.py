ans = 0;
a,b=0,0;
for c in input():
    if c=='0':
        ans = max(ans,b);
        a+=1;
        b=0;
    else:
        ans = max(ans,a);
        a=0;
        b+=1;
ans = max([ans, a,b]);
print(['NO','YES'][ans>6]);