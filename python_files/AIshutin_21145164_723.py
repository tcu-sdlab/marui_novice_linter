input()
s = input() + '_'
wr = 0
sep = 0
curr = 0
mx = 0
cnt = 0
for el in s:
    if el == '(':
        mx = max(mx, curr)
        wr = 1
        curr = 0
    if el == ')':
        if curr != 0:
            cnt += 1
        curr = 0
        wr = 0
    if el == '_':
        if wr == 0:
            mx = max(mx, curr)
            curr = 0
        else:
            if curr != 0:
                cnt += 1
            curr = 0
    if el != '_' and el != '(' and el != ')':
        curr += 1
    #print(mx, cnt, el)
print(mx , cnt)