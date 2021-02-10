n = int(input())
L = []
s = input()
count = 0
for i in s:
    if i == 'B':
        count += 1
    else:
        if count:
            L.append(count)
        count = 0
if count:
    L.append(count)
print(len(L))
print(*L)