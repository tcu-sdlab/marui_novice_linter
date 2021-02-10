n,s = list(input()), input();
n.sort(key=int);
for i in range (len(n)):
    if n[i]!='0':
        n[0],n[i]=n[i],n[0];
        break;
n=''.join(n);
print(['WRONG_ANSWER','OK'][n==s]);