n,m = [int(x) for x in input().strip().split(' ')]
unsafe = {}
for i in range(m):
    p,q = [int(x) for x in input().strip().split(' ')]
    if not unsafe.get(p):
        unsafe[p] = 0
    unsafe[p] += 1
    if not unsafe.get(q):
        unsafe[q] = 0
    unsafe[q] += 1

centre_point = 1
for i in range(1, n+1):
    if not unsafe.get(i):
        centre_point = i
        break
print(n-1)
for i in range(1, n+1):
    if i != centre_point:
        print(i, centre_point)