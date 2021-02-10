from collections import Counter

t = input
p = print
r = range
n = int(t())
s = Counter()
for i in range(n):
    s.update({t(): 1})
a = sorted(s, key=s.get)
p(a[-1])