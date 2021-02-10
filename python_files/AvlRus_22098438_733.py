s=input()
n=0;maxi=1
m='AEOUIYaeouiy'
for i in range(len(s)+1):
    if i<len(s) and not (s[i] in m) :n+=1
    elif n>0:
        if (n+1)>maxi :maxi=n+1
        n=0
print(maxi)