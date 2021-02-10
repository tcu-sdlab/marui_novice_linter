n = int(input())
a = list(map(int, input().split()))
result = 1
flag = False
res = 1
for i in a:
    if i == 1 and flag:
        result *= res
        res = 1
    if i == 1:
        flag = True
    if i == 0 and flag:
        res += 1
if not flag:
    print(0)
else:
    print(result)