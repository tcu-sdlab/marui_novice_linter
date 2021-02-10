n = input()
ans1 = 0
ans2 = 0
for i in n:
    if i == 'U':
        ans1 += 1
    elif i == 'D':
        ans1 -= 1
    elif i == 'R':
        ans2 += 1
    else:
        ans2 -= 1
ans1 = abs(ans1)
ans2 = abs(ans2)
if (ans1 % 2 == 0 and ans2 % 2 == 0) or (ans1 % 2 == 1 and ans2 % 2 == 1):
    print((ans1 + ans2) // 2)
else:
    print(-1)