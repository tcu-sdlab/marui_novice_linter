m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
d = 0
s1 = input()
s2 = input()
week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
s1 = week.index(s1)
s2 = week.index(s2)
z = abs(s1 - s2)
log = False
for d in range(7):
    summ = m[0] + d
    for i in range(1, 12):
        q = summ % 7
        summ += m[i]
        w = summ % 7
        if q == s1 and w == s2:
            log = True
if log:
    print('YES')
else:
    print('NO')