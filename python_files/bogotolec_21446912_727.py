cin = input().split(" ")
a = int(cin[0])
b = int(cin[1])
x = []
while (b > a):
    x.append(b)
    if (b % 10 == 1):
        b = (b - 1) // 10
    elif (b % 2 == 0):
        b //= 2
    else:
        break
x.append(b)
if (b == a):
    x.reverse()
    print("YES\n", len(x), sep = "")
    for i in x:
        print(i, end = " ")
else:
    print("NO")