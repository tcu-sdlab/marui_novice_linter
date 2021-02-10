n = int(input())
arr = [int(a) for a in input().split()]

if arr[n-1]==15:
    print('DOWN')
    exit()
if arr[n-1]==0:
    print('UP')
    exit()
if n==1:
    print('-1')
    exit()
if arr[n-1]>arr[n-2]:
    print('UP')
    exit()
print('DOWN')