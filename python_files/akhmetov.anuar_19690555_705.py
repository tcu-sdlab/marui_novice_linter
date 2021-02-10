t = input
p = print
r = range
n = int(t())
s1 = "I hate it"
s2 = "I love it"
s3 = "I hate that"
s4 = "I love that"
ans = [''] * n
for i in r(n -1):
    if i & 1:
        ans[i] = s4
    else:
        ans[i] = s3
p(' '.join(ans) + (s1 if n & 1 == 1 else s2))