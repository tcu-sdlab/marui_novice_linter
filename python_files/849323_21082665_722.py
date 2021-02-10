n = int(input())
p = [int(i) for i in input().split()]

s = []
for i in range(n):
    s.append(input())

check = True

for i in range(n):
    d = s[i].split()
    vowelcount = 0
    for j in d:
        for k in j:
            if k in 'aeiouy':
                vowelcount +=1
    if vowelcount != p[i]:
        check =False
        break

if check == False:
    print('NO')
else:
    print('YES')