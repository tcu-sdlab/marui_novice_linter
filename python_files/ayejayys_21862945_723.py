n, m = [int(x) for x in input().split(' ')]
arr = [int(x) for x in input().split(' ')]
d = {}
for i in range(1, m+1):
    d[i] = 0
av = n // m
for i in arr:
    if i <= m:
        d[i] += 1

ans = 0
for i in range(1, m+1):
    if d[i] < av:
        for j in range(n):
            if arr[j] <= m:
                if d[arr[j]] > av:
                    ans += 1
                    d[i] += 1
                    d[arr[j]] -= 1
                    arr[j] = i
                    if d[i] == av:
                        break
            else:
                ans += 1
                arr[j] = i
                d[i] += 1
                if d[i] == av:
                    break

print(av, ans)
print(' '.join(map(str, arr)))