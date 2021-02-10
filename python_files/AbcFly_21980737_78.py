sl = [input(),input(),input()];
nl = [5,7,5];
res = True;
for i in range(3):
    ans = 0;
    for c in sl[i]:
        if 'aeiou'.count(c):
            ans+=1;
    if ans!=nl[i]:
        res = False;
        break;
print(['NO','YES'][res]);