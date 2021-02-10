n = int(input())
s = input()
x = list(map(int, input().split()))
ans = 1000000001
r = s.find('R')
l = s.find('L')
if r!=-1 and l != -1:
    for i in range(0, n):
        if s[i] == 'R':
            r = i
        if s[i] == 'L':
            l = i
        if r < l:
            ans = min(ans, (x[l] - x[r])//2)

if ans == 1000000001:
    ans = -1
print(ans)