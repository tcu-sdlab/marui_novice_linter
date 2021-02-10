n = input()
s = input()
i = 0
ans = 0
while i <= len(s) - 1 and s[i] == '<':
    ans += 1
    i += 1
i = len(s) - 1
while i >= 0 and s[i] == '>':
    ans += 1
    i -= 1
print(ans)