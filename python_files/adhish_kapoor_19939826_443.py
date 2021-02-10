# cook your dish here
a=input()
a=list(a)
b=set()
for i in range(len(a)):
    if(a[i]!='{' and a[i]!='}' and a[i]!=',' and a[i]!=' '):
        b.add(a[i])
print(len(b))