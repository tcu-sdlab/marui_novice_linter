ip = input()
it=list(ip)
c = 0
pre = it[c]
count = 0
flag = 0
while c<len(ip):
    cur = it[c]
    if pre == cur:
        count+=1
    else:
        count = 0
    if count >= 6:
        flag = 1
        break
    c+=1
    pre = cur
if flag == 1:
    print('YES')
else:
    print('NO')