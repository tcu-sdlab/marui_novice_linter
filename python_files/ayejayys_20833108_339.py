n, m = [int(x) for x in input().strip().split(' ')]
arr = map(lambda x:int(x), input().strip().split(' '))
state = 1
ans = 0
for j in arr:
    if j < state:
        ans += n-state+j
    else:
        ans += j-state
    state = j
print(ans)