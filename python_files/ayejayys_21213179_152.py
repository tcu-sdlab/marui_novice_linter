n, m = [int(x) for x in input().split(' ')]
d = [0]*m
arr = [''] * n
for i in range(n):
    arr[i] = input()

for i in range(m):
    local_dict = dict()
    for j in range(n):
        if not local_dict.get(arr[j][i]):
            local_dict[arr[j][i]] = 0
        local_dict[arr[j][i]] += 1
    d[i] = len(local_dict)

ans = 1

mod = 10**9+7
for i in range(m):
    ans = (ans*d[i])%mod
print(ans)