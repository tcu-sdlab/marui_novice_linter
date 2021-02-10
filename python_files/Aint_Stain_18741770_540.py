a=int(input())
b=input()
c=input()
j=0
for i in range(a):
    x=(abs(int(b[i])-int(c[i])))
    y=10-x
    j+=min(x,y)
print(j)