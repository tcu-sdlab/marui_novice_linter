n, k = [int(x) for x in input().split(' ')]
arr = [int(x) for x in input().split(' ')]
if n == 1:
    print(0)
    print(arr[0])
else:
    diff = 0
    for i in range(1, n):
        if arr[i] +arr[i-1] < k:
            diff += k - (arr[i]+arr[i-1])
            arr[i] = k - arr[i-1]
    
    print(diff)
    print(' '.join([str(x) for x in arr]))