def indef(s):
    global ans, kop
    strs = [x for x in s.split('.')]
    if len(strs) == 1:
        ans += int(strs[0])
    else:
        res = ""
        for i in range(len(strs) - 1):
            res += strs[i]
            
        if len(strs[-1]) < 3:
            kop += int(strs[-1])
        else:
            res += strs[-1]
        
        ans += int(res)
    
    
ans = 0
kop = 0

s = input()

a = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]


add = ""

sums = []

for i in s:
    if not i in a:
        if add != "":
            sums.append(add)
        add = ""
    else:
        add += i
if add != "":
    sums.append(add)

for i in sums:
    indef(i)
    
ans += (kop // 100)
kop %= 100

ans = str(ans)
j = 0

result = ""
for i in range(len(ans) -1, -1, -1):
    result += ans[i]
    j += 1
    
    if j % 3 == 0 and i != 0:
        result += '.'
        
result = result[::-1]

if kop != 0:
    if kop < 10:
        charr = "0"
    else:
        charr = ""
    result += "." + charr + str(kop)



print(result)