input()
s = input()
a = [0] * 10
for i in s:
    a[int(i)] = 1
ok = "YES"
if a[1] + a[2] + a[3] == 0 or a[1] + a[4] + a[7] + a[0] == 0 or a[3] + a[6] + a[9] + a[0] == 0 or a[7] + a[0] + a[9] == 0:
    ok = "NO"
print(ok)