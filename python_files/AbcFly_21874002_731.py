ms = 'abcdefghijklmnopqrstuvwxyz';
ds = input();
if ds[0]!='a':
   ds='a'+ds; 
ans=0
for i in range(1,len(ds)):
    s = abs(ms.index(ds[i])-ms.index(ds[i-1]));
    t = 26-s;
    ans+=min(s,t);
print(ans)