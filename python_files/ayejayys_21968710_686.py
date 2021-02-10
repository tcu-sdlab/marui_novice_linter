n = int(input())
arr = [int(x) for x in input().split(' ')]
while True:
    change = False
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            change = True
            arr[i], arr[i+1] = arr[i+1], arr[i]
            print(i+1, i+2)
    if not change:
        break