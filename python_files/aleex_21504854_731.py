n = int(input())
a = [0] * n
a = list(map(int, input().split()))
a.append(0)
ok = int(0)
for i in range(n) :
    if a[i] % 2 == 1 :
        if i == n + 1 :
            ok = 1
        elif a[i + 1] == 0 : 
            ok = 1
        else :
            a[i + 1] -= 1
if ok == 0: 
    print("YES")
else :
    print("NO")