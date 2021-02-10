n = int(input())
arr = [int(i) for i in input().split()]
arr.sort()
if n % 2 == 0:
    print(arr[n // 2 - 1])
else:
    print(arr[n // 2])