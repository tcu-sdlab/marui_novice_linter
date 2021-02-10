n, m = [int(x) for x in input().split(' ')]
colored = False
colors = ['C', 'M', 'Y']
for i in range(n):
    arr = input().split(' ')
    for j in arr:
        if j in colors:
            colored = True
            break
    if colored:
        break
print('#Color' if colored else '#Black&White')