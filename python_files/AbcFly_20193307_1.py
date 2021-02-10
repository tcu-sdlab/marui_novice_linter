def A2B(item):
    result='R'+item[1]+'C'
    column=0
    digit=len(item[0])-1
    for ch in item[0]:
        column += (26**digit) * (ord(ch)-ord('A')+1)
        digit -= 1
    result+=str(column)
    return result

def B2A(item):
    column=int(item[3])
    res=[]     
    while column>0:
        res.append(chr(column-(column-1)//26*26 + ord('A')-1))
        column = (column-1)//26
    res.reverse()
    return ''.join(res)+item[1]

def trans(item):
    if len(item[2])==0 and len(item[3])==0:
        return A2B(item[:2])
    else:
        return B2A(item)

def section(string):
    result=['','','','']
    flag=True
    for ch in string:
        if len(result[1])!=0 and ch.isalpha():
            flag=False
        if flag==True:
            if ch.isalpha():
                result[0]+=ch
            if ch.isdigit():
                result[1]+=ch
        if flag==False:
            if ch.isalpha():
                result[2]+=ch
            if ch.isdigit():
                result[3]+=ch
    return result

def translate(cells):
    for cell in cells:
        print(trans(section(cell)))
    return


n=int(input())
ans=[]
for i in range(n):
    ans+=[input()]
translate(ans)