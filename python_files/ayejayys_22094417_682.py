n = int(input())
arr = [int(x) for x in input().split(' ')]
arr = sorted(arr)
i = 1
for j in arr:
    if j >= i:
        i+=1
print(i)