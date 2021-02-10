a = input()
n = ''
summ = 0
def obr(n):
    summ = 0
    p = 0
    for i in range(-1, -len(n) - 1, -1):
        if n[i] !='.' and i == -3 or len(n) < 3:
            summ *= 100
            p += 2
        if n[i] != '.':
            summ += int(n[i]) * (10 ** p)
            p += 1
    return summ
    
    
for i in a:
    if 'a' <= i <= 'z':
        if n != '':
            summ += obr(n)
            n = ''
    else:
        n += i
if n != '':
    summ += obr(n)

ans = str(summ)
if summ < 100:
    while len(ans) < 3:
        ans = '0' + ans

n = len(ans)

if ans[-2:] == '00':
    ans = ans[:-2]
    n -= 2
    i = -3
    l = 0
else:
    ans = ans[:-2] + '.' + ans[-2:]
    l = 1
    i = -6
while i > -n - l:
    ans = ans[:i] + '.' + ans[i:]
    i -= 4
    l += 1
print(ans)