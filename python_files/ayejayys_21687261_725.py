n = int(input())
s = input()
pos = None
rights = 0
lefts = 0
for i in range(n-1):
    if s[i] == '>' and s[i+1] == '<':
        pos = i
        break
    elif s[i] == '<':
        lefts += 1

if pos != None:
    for i in range(n-1, pos+1, -1):
        if s[i] == '<' and s[i-1] == '>':
            break
        elif s[i] == '>':
            rights += 1

    print(lefts+rights)
else:
    print(n)