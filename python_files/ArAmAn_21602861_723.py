n = int(input())
s = input()
s += '_'
skob = 0
cnt = 0
maxL = 0
word = ''
for i in range(len(s)):
    cur = s[i]
    if cur == '_':
        if skob > 0 and len(word) != 0:
            cnt += 1
        else:
            if len(word) != 0:
                if len(word) > maxL:
                    maxL = len(word)
        word = ''
    elif cur == '(':
        if skob == 0:
            if len(word) > maxL:
                maxL = len(word)
        else:
            cnt += 1
        skob += 1
        word = ''
    elif cur == ')':
        if s[i - 1] != '_' and s[i - 1] != '(':
            cnt += 1
        word = ''
        skob -= 1
    else:
        word += cur
print(maxL, cnt)