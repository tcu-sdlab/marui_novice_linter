# contest/733/problem/0

s = input()+'A'

pr = 0
i = -1
st = -1
while i < len(s):
    if s[i] in set('AEIOUY'):
        cpr = i - st
        if cpr > pr:
            pr = cpr
        st = i
    i += 1

print(pr)