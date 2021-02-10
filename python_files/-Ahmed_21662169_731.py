odd = 0
invalid = 0
w = input()
a = [a.strip() for a in input().split(" ")]

for i in range(0, len(a), 1):
    x = int(a[i])
    if odd:
        if x > 1 and (x % 2 == 0):
            odd = 1
        elif x > 0:
            odd = 0
        else:
            invalid = 1
    elif x % 2 == 1:
        odd = 1

if invalid or odd:
    print("NO\n")
else:
    print("YES\n")