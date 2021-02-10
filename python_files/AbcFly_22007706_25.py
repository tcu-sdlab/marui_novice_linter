n = int(input());
sl = input();
ans=[];
for i in range(n):
    ans+=[sl[i]];
    if i%2 and i<(n-(n%2)-2):
        ans+=['-'];
print(''.join(ans));