def sostoyanie(simvol):
    global sost
    global temp_rub
    global sum
    global sumkop
    global temp_kop
    if sost == 0:
        if simvol.isalpha():
            return
        else:
            temp_rub += simvol
            sost = 1
            return
    if sost == 1:
        if simvol == '.':
            sost = 2
            return
        elif simvol.isalpha():
            sum += int(temp_rub)
            temp_rub = str()
            sost = 0
        else:
            temp_rub += simvol
    if sost == 2:
        if simvol.isalpha():
            if len(temp_kop) == 2:
                sumkop += int(temp_kop)
                sum += int(temp_rub)

            temp_kop = str()
            sost = 0
            temp_rub = str()
            return
        else:
            temp_kop += simvol
            if len(temp_kop) > 2:
                temp_rub += temp_kop
                temp_kop = str()
                sost = 1
                return


sost = 0
rubbles = []
temp_rub = str()
temp_kop = str()
sum = 0
sumkop = 0
s = input()
s += 'a'


for i in range(len(s)):
    sostoyanie(s[i])
temp = sumkop // 100
sum += temp
sumkop -= temp * 100
temp = 0
sum = str(sum)
ans = str()
for i in range(len(sum) - 1, -1, -1):
    if temp < 3:
        ans += sum[i]
    else:
        ans += '.'
        ans += sum[i]
        temp = 0
    temp += 1
ans = ans[::-1]
if sumkop == 0:
    print(ans)
else:
    print(ans, str(sumkop).rjust(2, '0'), sep='.')