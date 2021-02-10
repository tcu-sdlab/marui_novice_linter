from math import *
n = int(input())
A = list(map(int, input().split()))
ans = set()
for i in range(n):
    ans.add(A[i])
t = len(ans)
if t == 1:
    print('YES')
elif t == 2:
    print('YES')
elif t == 3:
    per1 = ans.pop()
    per2 = ans.pop()
    per3 = ans.pop()
    s1 = max(per1, per2, per3)
    s3 = min(per1, per2,per3)
    s2 = per1 + per2 + per3 - s1 - s3
    if s1 - s2 == s2 - s3:
        print('YES')
    else:
        print('NO')
else:
    print('NO')