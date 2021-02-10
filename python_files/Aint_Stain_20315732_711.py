n = int(input())
list = []
for i in range(n):
    list.append(input())

flag = 0
for i in range(n):
    ara = list[i]
    if(ara[0:2]=="OO"):
        flag = 1
        list[i] = '++'+ara[2:5]
        break
    if(ara[3:5]=="OO"):
        flag = 1
        list[i] = ara[0:3]+'++'
        break
if(flag==1):
    print("YES")
    for ara in list:
        print(ara)
else:
    print("NO")