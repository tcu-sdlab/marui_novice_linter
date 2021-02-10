a=int(input())
b=input()
c=input()
j=0
i=0
while i<a:
    x=(abs(int(b[i])-int(c[i])))
    y=10-x
    j+=min(x,y)
    i+=1
print(j)