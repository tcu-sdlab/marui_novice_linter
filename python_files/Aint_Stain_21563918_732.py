sizeofara, walknumber = map(int, input().split())
ara = list(map(int, input().split()))
count = 0
for i in range(0, sizeofara - 1):
    x = ara[i] + ara[i + 1]
    if x < walknumber: 
        count += walknumber - x
        ara[i + 1] += walknumber - x
print(count)
print(*ara)