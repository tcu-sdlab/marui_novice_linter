count=0
list=[]*0

ara1=str(input())
x1=ord(ara1[0])-ord('a')
y1=int(ara1[1])

ara2=str(input())
x2=ord(ara2[0])-ord('a')
y2 =int(ara2[1])

while x1!=x2 or y1!=y2:
    str=""
    if x1>x2:
        str="L";
        x1-= 1
    else:
        if x1<x2:
            str="R";
            x1+= 1
    if y1<y2:
        str+="U";
        y1 += 1
    else:
        if y1>y2:
            str+="D";
            y1-=1
    list.append(str);
    count+= 1
print(count)

for string in list:
    print(string)