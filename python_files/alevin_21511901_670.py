a = int(input().strip())

min_h = 0
max_h = 0

if a <= 5:
    min_h = 0
elif a <= 7:
    min_h = a - 5
else:
    min_h = 2 * (a // 7)
    if a % 7 == 6:
        min_h += 1

if a == 1:
    max_h = 1
elif a > 1 and  a <= 7:
    max_h = 2
else:
    max_h = 2 * (a // 7)
    if a % 7 == 1:
        max_h += 1
    elif a % 7 >= 2:
        max_h += 2


print(min_h, max_h)