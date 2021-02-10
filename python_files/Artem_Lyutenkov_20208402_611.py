a = input().split()
b = int(a[0])
if a[2] == 'week':
    if b >= 5 and b <= 6:
        print(53)
    else:
        print(52)
else:
    if b == 31:
        print(7)
    elif b == 30:
        print(11)
    else:
        print(12)