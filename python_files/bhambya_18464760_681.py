ok = False
t = int(input())
for _ in range(t):
    n, b, a = input().split()
    b = int(b)
    a = int(a)

    if b >=2400 and a > b:
        ok = True

print("YES" if ok else "NO")