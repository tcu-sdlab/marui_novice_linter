os = 'AEIOUY';
cs = input()+'A';
ans=1;
Last=-1;
for c in range(len(cs)):
    if os.count(cs[c])>0:
        ans=max(ans, c-Last);
        Last = c;
print(ans);