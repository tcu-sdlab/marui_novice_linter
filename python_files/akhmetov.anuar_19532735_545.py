t = input
r = range
s1 = t()
s2 = t()
p = []
c = 0
for i1, i2 in zip(s1, s2):
    if i1 != i2:
        p.append(i1 if c else i2)
        c = 1 - c
    else:
        p.append(i1)
print('impossible' if c else ''.join(p))