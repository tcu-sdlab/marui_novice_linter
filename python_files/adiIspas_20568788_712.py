numbers = int(input())

a = []
b = []

# for i in range(0, numbers):
#     a.append(int(input()))

a = list(map(int, input().split()))

for i in range(1, numbers):
    b.append(a[i - 1] + a[i])

b.append(a[numbers - 1])
# print(b)
print(" ".join(list(map(str, b))))