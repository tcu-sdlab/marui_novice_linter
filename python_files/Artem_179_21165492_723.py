n = int(input())
a = '_' + input() + '_'
n+= 2
per = 0
left = 0
a1 = []
a2 = []
for j in range(n):
    if a[j] == '(':
        per = 1
        if left != 0:
            a2.append(a[left:j])
        left = j +1
    elif a[j] == ')':
        per = 0
        a1.append(a[left:j])
        left = j+1
    elif a[j] == '_':
        if left == 0:
            left = 1
        else:
            if per == 1:
                a1.append(a[left:j])
            else:
                a2.append(a[left:j])
            left = j+1
maxs = -float('infinity')
for j in range(len(a2)):
    if a2[j] != '':
        maxs = max(maxs, len(a2[j]))
if maxs != -float('infinity'):
    print(maxs, end = ' ')
else:
    print(0, end = ' ')
score = 0
for j in range(len(a1)):
    if a1[j] != '':
        score += 1
print(score)