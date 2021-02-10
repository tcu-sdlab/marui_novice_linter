s = input()
for i in range(len(s)):
    if (s[i] >= '5' and not(i == 0 and s[i] == '9')):
        s = s[:i] + str(9 - int(s[i])) + s[i + 1:]
print(int(s))