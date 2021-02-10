n,m = map(int, input().split());
sl = [];
ans = True;
for i in range(n):
    st = input();
    sl+=[st[0]];
    if m!=st.count(st[0]):
        ans = False;
if ans:
    for i in range(1, n-1):
        if sl[i]==sl[i-1] or sl[i]==sl[i+1]:
            ans = False;
            break;
print(['NO','YES'][ans]);