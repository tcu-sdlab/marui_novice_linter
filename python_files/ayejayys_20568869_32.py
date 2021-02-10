import re
n, d = list(map(lambda x:int(x), re.split("\s+", input().strip())))
arr = list(map(lambda x:int(x), re.split("\s+", input().strip())))
arr.sort()
ans = 0
for i in range(n):
    j = i-1
    while j >= 0:
        if (arr[i]-arr[j] > d):
            break
        else:
            j-=1
    ans += 2*(i-1-j)

print(ans)