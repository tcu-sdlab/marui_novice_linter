import sys
fl = lambda: sys.stdout.flush()

n = int(input())

print('? 1 2')
fl()
x = int(input())
print('? 1 3')
fl()
y = int(input())
print('? 2 3')
fl()
z = int(input())

arr = [None for i in range(n)]
arr[0] = (x+y-z) // 2
arr[1] = (x+z-y) // 2
arr[2] = (y+z-x) // 2

for i in range(3, n):
    print('? %i %i' % (i, i+1))
    fl()
    s = int(input())
    arr[i] = s - arr[i-1]

print('! ', end = '')
print(*arr)