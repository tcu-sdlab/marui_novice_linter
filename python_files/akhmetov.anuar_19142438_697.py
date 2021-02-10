s = input()
a, b = s.split('e')
index = a.find('.')
ans = ''
if index == -1:
    b = '0' * (int(b))
    ans = a + b
else:
    a1, a2 = a[:index], a[index + 1:]
    if(int(a2) == 0):
        ans = a1 + '0' * int(b)
    elif len(a2) <= int(b):
        ans = a1 + a2 + '0' * (int(b) - len(a2))
    else:
        a2 = a2[:int(b)] + '.' + a2[int(b):]
        ans = a1 + a2

print(ans)