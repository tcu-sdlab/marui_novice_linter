n = int(input())
mat = input()
lis = []
cnt = 0
last = False
for c in mat:
    if c == 'B':
        if not last:
            last = True
            cnt += 1
            lis.append(1)
        else:
            lis[-1] += 1
    else:
        last = False

print(cnt)
for k in lis:
    print(k, end=' ')

if cnt:
    print()