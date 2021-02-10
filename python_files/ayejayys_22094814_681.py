n = int(input())
i = 0
changed = True
found = False
while changed:
    j = 0
    changed = False
    while i*1234567 + j*123456 <= n:
        s = i*1234567 + j*123456
        if s == n or ((n-s)% 1234 == 0):
            found = True
            changed = False
            break
        changed = True
        j += 1
    i += 1
print("YES" if found else "NO")