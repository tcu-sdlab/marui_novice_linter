length = int(input())
string = input()
outer = ""
inner = ""

i = 0
while i < length:
    if string[i] == '(':
        i += 1
        inner += " "
        while string[i] != ')':
            if string[i] != '_' and string[i] != '&':
                inner += string[i]
            else:
                inner += " "
            i += 1
        if string[i] == ')':
            outer += " "
    else:
        if string[i] != '_' and string[i] != '&':
            outer += string[i]
        else:
            outer += " "
    i += 1
        
outer = outer.split()
inner = inner.split()

if outer == []:
    print(0, end=" ")
else:
    len_o = []
    for i in outer:
        len_o.append(len(i))
    print(max(len_o), end=" ")

print(len(inner))