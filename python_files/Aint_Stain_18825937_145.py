a=list(input())
b=list(input())
x=0
y=0
for i in range(len(a)):
    if a[i]=='4' and b[i]=='7':
        x+=1
    elif a[i]=='7' and b[i]=='4': 
        y+=1
print(max(x,y))