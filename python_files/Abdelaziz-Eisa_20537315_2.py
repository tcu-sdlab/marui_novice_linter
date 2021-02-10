r = []
p = {}
t = {}

for i in range(int(input())):
    n, s = input().split()
    s = int(s)
    r.append((n, s))
    
    if n in p:
        p[n] += s
    else:
        p[n] = s
    
m = max(p.values())

for k, v in p.items():
    if v == m:
        t[k] = 0

for i in r:
    if i[0] not in t:
        continue
    
    t[i[0]] += i[1]

    if (t[i[0]] >= m):
        print(i[0])
        break