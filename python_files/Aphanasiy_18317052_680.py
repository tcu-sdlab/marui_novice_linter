def get(m, k, mp):
    i = m - k
    j = m + k
    if i < 0 and j < n:
        return mp[j]
    elif i >= 0 and j >= n:
        return mp[i]
    elif i >= 0 and j < n and (mp[i] ^ mp[j]) == 0:
        return mp[i] + mp[j]
    else:
        return 0
        
        
n, m = map(int, input().split())
m -= 1
mp = list(map(int, input().split()))
i = m
j = m
ans = mp[m]
for k in range(1, 101):
    ans += get(m, k, mp)
print(ans)