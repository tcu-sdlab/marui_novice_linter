n, t = map(int, input().split())
s = set()
for i in range(n):
    s.add(input().strip())
d = dict()
for i in s:
    if len(i) not in d:
        d[len(i)] = 0
    d[len(i)] += 1
k = sorted(d.items())
s = len(input().strip())
mn = 0
mx = 0
ans = 0
for i in k:
    if i[0] == s:
        mn = ans + 1
        mx = ans + i[1]
        break
    ans += i[1]
print(mn + (max(0, (mn - 1) // t) * 5) , 
      mx + (max(0, (mx - 1) // t) * 5) )