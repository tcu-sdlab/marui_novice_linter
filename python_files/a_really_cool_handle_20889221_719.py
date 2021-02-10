n = int(input())
a = input().strip()
even = a[::2]
odd = a[1::2]

c = 'rb'
ans = n

for i in range(2):
    x = len(even) - even.count(c[i])
    y = len(odd) - odd.count(c[i^1])
    ans = min(ans, max(x,y))

print (ans)