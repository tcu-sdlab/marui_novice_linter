n = int(input())
a = input().split()
per = 0
for i in a:
    if i == '0':
        per+=1
if n != 1:
    if per == 1:
        print('YES')
    else:
        print('NO')
else:
    if per == 0:
        print('YES')
    else:
        print('NO')