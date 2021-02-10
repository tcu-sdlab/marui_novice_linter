a = input().strip().lower()
b = input().strip().lower()
if a == b:
    print(0)
elif b > a:
    print(-1)
else:
    print(1)