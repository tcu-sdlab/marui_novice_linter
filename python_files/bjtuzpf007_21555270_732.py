n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
raw_sum = sum(a)
for i in range(1, len(a)):
    a[i] = max(k - a[i - 1], a[i])
print(sum(a) - raw_sum)
for i in a:
    print(i, end=' ')