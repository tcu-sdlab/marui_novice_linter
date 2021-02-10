import math

num = input()

a, b = num.split('e')
a, c = a.split('.')

b = int(b)

erg = a + c[:b]

erg += "0" * max(0, b - len(c))

c = c[b:]
c = c.rstrip('0')
if c:
    erg = erg + "." + c

erg = erg.lstrip('0')
if not erg:
    erg = '0'
if erg[0] == '.':
    erg = '0' + erg

print(erg)