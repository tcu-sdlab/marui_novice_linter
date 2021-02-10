m, n = [int(x) for x in input().split(' ')]
dm = {}
dn = {}
for i in range(5):
    dm[i] = m//5 + ((m%5) >= i)
    dn[i] = n//5 + ((n%5) >= i)
ans = (dm[0]-1)*(dn[0]-1)
for i in range(1, 5):
    ans += dm[i]*dn[5-i]
print(ans)