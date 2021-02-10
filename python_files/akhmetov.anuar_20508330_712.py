t = input
p = print
r = range
a = t()
counter = [0] * 4
for i in a:
    if i == 'L':
        counter[0] += 1
    elif i == 'R':
        counter[1] += 1
    elif i == 'U':
        counter[2] += 1
    else:
        counter[3] += 1
ans = -1
if len(a) & 1 == 0:
    LR = abs(counter[0] - counter[1])
    DU = abs(counter[2] - counter[3])
    ans = (LR + DU) // 2

print(ans)