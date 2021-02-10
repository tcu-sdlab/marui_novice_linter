n, x = [int(x) for x in input().split(' ')]
d = 0
for i in range(n):
    sign, am = input().split(' ')
    am = int(am)
    if sign == '+':
        x += am
    else:
        if x >= am:
            x -= am
        else:
            d += 1
print(x, d)