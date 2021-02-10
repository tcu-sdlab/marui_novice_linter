i=int(input())
l=input().split()
li=[int(i) for i in l]
size=0
data=0
temp=0
for i in li:
    if i > data:
        temp+=1
        data=i
    else:
        data=i
        if temp > size:
            size=temp
        temp=1
if temp > size:
    size=temp
print(size)