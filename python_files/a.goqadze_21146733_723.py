input()
s = input() + "_"

cnt = 0
in_parentheses = False
lw = 0
nw = 0

for c in s:
    if c is '_':
        if in_parentheses:
            nw += cnt > 0
        else:
            lw = max(lw, cnt)
        cnt = 0
    elif c is '(':
        in_parentheses = True
        lw = max(lw, cnt)
        cnt = 0
    elif c is ')':
        in_parentheses = False
        nw += cnt > 0
        cnt = 0
    else:
        cnt += 1

print("%d %d" % (lw, nw))