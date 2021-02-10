n, m = map(int, input().split())
A = [0] * n
for i in range(n):
    A[i] = list(map(str, input().split()))
per = True
for i in range(n):
    for j in range(m):
        if A[i][j] == 'Y' or A[i][j] == 'M' or A[i][j] == 'C':
            per = False
            break
if per:
    print('#Black&White')
else:
    print('#Color')