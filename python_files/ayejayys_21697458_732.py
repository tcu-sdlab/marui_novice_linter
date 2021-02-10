k, r = [int(x) for x in input().split()]
last = k%10
p = last
ans = 1
while p != 0 and p != r:
    ans += 1
    p = (last*ans)%10
print(ans)