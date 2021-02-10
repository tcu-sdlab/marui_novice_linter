cnt_b1, cnt_r1, cnt_b2, cnt_r2 = 0, 0, 0, 0
num = input()
s = input()
for i, c in enumerate(s):
    if i % 2 == 0:
        if c == 'r':
            cnt_r1 += 1
        else:
            cnt_b1 += 1
    else:
        if c == 'r':
            cnt_r2 += 1
        else:
            cnt_b2 += 1
print(min(max(cnt_b2, cnt_r1), max(cnt_r2, cnt_b1)))