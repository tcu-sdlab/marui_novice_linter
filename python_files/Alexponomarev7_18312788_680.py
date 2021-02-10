n, a = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
ss = sum(arr)

a -= 1
ans = 0
ss -= arr[a]
for i in range(1, a + 1):
    if a + i < n:
        if (arr[a - i] + arr[a + i]) == 2:
            ans += 2
        
        ss -= arr[a - i]
        ss -= arr[a + i]
        
ans += arr[a]
ans += ss
print(ans)