n, a, b = [int(x) for x in input().split(' ')]
tmp = (a+b)%n
if tmp < 0:
    tmp = n+tmp
elif tmp == 0:
    tmp = n
print(tmp)