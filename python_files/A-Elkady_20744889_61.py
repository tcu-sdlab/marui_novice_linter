x=input()
y=input()
c=''
for i in range(len(x)):
    if x[i]==y[i]:c=c+'0'
    else: c=c+'1'
print(c)