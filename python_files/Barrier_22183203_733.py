n = int(input())
a = []
ans = 0
L,R = 0,0
for i in range(n):
    t = input().split()
    L += int(t[0])
    R += int(t[1])
    a.append(t)
Max = abs(L-R)
for i in range(n):
    l = L - int(a[i][0]) + int(a[i][1])
    r = R - int(a[i][1]) + int(a[i][0])
    if abs(l-r) > Max:
        Max = abs(l-r)
        ans = i+1
print(ans)