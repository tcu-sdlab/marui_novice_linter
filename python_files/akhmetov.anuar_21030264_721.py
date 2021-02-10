from collections import Counter

t = input
p = print
r = range
n, k = map(int, t().split())
pasw = []
for i in r(n):
    pasw.append(t())

password = t()
pasw.sort(key=len)
c = 0
best_found = False
l = 0
for i in r(n):
    if len(pasw[i]) == len(password):
        if best_found:
            l += 1
        best_found = True
    if len(pasw[i]) < len(password):
        c += 1
b = (c // k) * 5 + c + 1
p(b, b + ((l + c % k) // k) * 5 + l)