n = int(input())
a = list(map(int, input().split()))

for i in range(0, len(a)):
    if i == len(a) - 1:
        if a[i] % 2 != 0:
            print("NO")
            exit()
        else:
            print("YES")
            exit()
    if a[i] % 2 == 0:
        continue
    else:
        a[i+1] -= 1
        a[i] -= 1
        if a[i+1] < 0 or a[i] < 0:
            print("NO")
            exit()
print("YES")