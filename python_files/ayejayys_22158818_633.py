m = int(input())
num = 0
x = 0
while x < m:
    num += 5
    tmp = num
    while tmp%5 == 0:
        x += 1
        tmp = tmp//5
    if x == m:
        break

if x == m:
    print(5)
    for i in range(5):
        print(num+i, end = " ")
    print()
else:
    print(0)