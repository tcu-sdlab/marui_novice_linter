n, a = [int(x) for x in input().split(' ')]
arr = [int(x) for x in input().split(' ')]
a -= 1
ans = arr[a]
i = a-1
j = a+1
while i>=0 and j < n:
    ans += 2 if (arr[i] and arr[j]) else 0
    i-=1
    j+=1
while i>=0:
    ans += arr[i]
    i-=1
while j<n:
    ans += arr[j]
    j += 1
print(ans)