n, c = map(int, input().split())
a = [int(s) for s in input().split()]

count = 1

for i in range(n - 1):
    if ((a[i + 1] - a[i]) <= c):
        count += 1
    else:
        count = 1

print(count)