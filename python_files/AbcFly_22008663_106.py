md = {"6":1,"7":2, "8":3, "9":4, "T":5, "J":6, "Q":7, "K":8,"A":9};
c = input();
a,b = input().split();
ans = False;
if a[1]==b[1]:
    if md.get(a[0])>md.get(b[0]):
        ans=True;
elif a[1]==c:
    ans=True;
print(['NO','YES'][ans]);