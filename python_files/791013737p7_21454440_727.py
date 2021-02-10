n = input().split()
a = int(n[0])
b = int(n[1])
result = list()
while b > a:
    if b % 10 == 1:
        result.append(b)
        b /= 10
        b = int(b)
    elif b % 2 == 1:
        print("NO")
        exit()
    else:
        result.append(b)
        b /= 2
result.append(a)
if b < a:
    print("NO")
    exit()
print("YES")
print(len(result))
r = ''
for i in result:
    r = str(int(i)) + ' ' + r
print(r)