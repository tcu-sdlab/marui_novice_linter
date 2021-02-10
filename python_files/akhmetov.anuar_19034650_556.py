n = int(input())
a = list(map(int, input().split()))
ok = "No"
for j in range(n):
    for i in range(n):
        if i & 1 == 1:
            a[i] = (a[i] - 1) % n if a[i] != 0 else n - 1
        else:
            a[i] = (a[i] + 1) % n
    if a == sorted(a) and len(a) == len(set(a)):
        ok = "Yes"
print(ok)