n = int(input().strip())
arr = list(set(map(lambda x: int(x), input().strip().split(' '))))
arr.sort()
if (len(arr) <= 1):
    print("NO")
else:
    print(arr[1])