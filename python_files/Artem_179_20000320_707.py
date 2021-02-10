from math import *
n = int(input())
if n % 2 == 1:
    n *= n
    if n == 1:
        print(-1)
    else:
        print(n // 2 , n // 2 + 1)
else:
    if n == 2:
        print(-1)
    else:
        n *= n
        print(-1 + n // 4, 1 + n // 4)