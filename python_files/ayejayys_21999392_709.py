s = list(input())
i = 0
while i < len(s) and s[i] == 'a':
    i+=1
if i == len(s):
    s[-1] = 'z'
else:
    while i < len(s) and s[i] != 'a':
        s[i] = chr(ord(s[i])-1)
        i += 1
print(''.join(s))