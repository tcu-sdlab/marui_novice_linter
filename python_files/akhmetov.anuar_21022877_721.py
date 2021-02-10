t = input
p = print
r = range

n = int(t())
s = t()

col = []
c = 0
for i in r(len(s)):
    if s[i] == "B":
        c += 1
        if i == n - 1:
            col.append(c)
    else:
        if c != 0:
            col.append(c)
        c = 0
if sum(col) == 0:
    p(0)
else:
    p(len(col))
    p(' '.join(map(str, col)))