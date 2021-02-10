n = int(input())
s = input()
in_paren = False
words = 0
mx = 0
j = 0 #length of current word
for i in s:
    if i == "_":
        words += 1 if in_paren and j else 0
        if not in_paren:
            mx = max(mx, j)
        j = 0
    elif i == "(":
        in_paren = True
        mx = max(mx, j)
        j = 0
    elif i == ")":
        words += 1 if in_paren and j else 0
        in_paren = False
        j = 0
    else:
        j += 1
mx = max(mx, j)
print(mx, words)