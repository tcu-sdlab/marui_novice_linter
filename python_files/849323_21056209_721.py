ss = input()

n,k = int(ss.split()[0]),int(ss.split()[1])

password = [""] * n

for i in range(n):
    password[i] = input()

s  = input()

from collections import defaultdict

d = defaultdict(int)

for i in range(n):
    d[len(password[i])] +=1

pred = 0

for i in range(1,len(s)):
    pred += d[i]

mind = pred + (pred//k) * 5 + 1
pred += d[len(s)]

if pred%k == 0:
    maxd = pred + (pred//k - 1) * 5
else:
    maxd = pred + (pred//k) * 5

print(mind,maxd)