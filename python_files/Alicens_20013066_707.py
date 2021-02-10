import math

n = int(input())

if n % 2 == 0:

    n //= 2
    m, n = n, 1

    a = m**2 - n**2
    c = m**2 + n**2

else:
    a = (n**2-1) // 2
    c = a + 1

if not a or not c:
    print("-1")
    exit(0)

print("{} {}".format(a, c))