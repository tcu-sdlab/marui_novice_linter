t = input
p = print
r = range
s = t()
if s.count('0') == 0:
    p(s[1:])
else:
    i = s.find('0')
    p(s[0:i]+s[i+1:])