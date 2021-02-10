a = [int(x) for x in input().split()]
ans = sum(a)

ar = dict()
for i in a:
    if i in ar:
        ar[i] = ar[i] + 1
    else:
        ar[i] = 1

l = -1000
for i in ar:
    if i > 0:
        if (l == -1000 or min(ar[i], 3) * i > min(ar[l], 3) * l) and (ar[i] >= 2):
            l = i

if l != -1000:
    ans -= min(ar[l], 3) * l
    
print(ans)