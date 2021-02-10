from collections import defaultdict
import sys, os, math

if __name__ == "__main__":
    #n, m = list(map(int, input().split()))
    a00, a01, a10, a11 =  map(int, input().split())
    x, y = int((1 + math.sqrt(1 + 8 * a11)) // 2), int((1 + math.sqrt(1 + 8 * a00)) // 2)
    if a11 + a10 + a01 + a00 == 0:
        print(1)
        sys.exit(0)
    elif a11 + a10 + a01 == 0 and y * (y - 1) // 2 == a00:
        print('0' * y)
        sys.exit(0)
    elif a00 + a10 + a01 == 0 and x * (x - 1) // 2 == a11:
        print('1' * x)
        sys.exit(0)
    if y * (y - 1) // 2 != a00 or x * (x - 1) // 2 != a11 or x * y != a10 + a01:
        print("Impossible")
        sys.exit(0)
    l = x - math.ceil((x * y - a10) / y) #no.of left one
    r = (x * y - a10) // y #no.of right one
    diff = a10 - l * y
    #print("x, y, l, r, diff")
    #print(x, y, l, r, diff)
    if diff == 0:
        print('1' * l + '0' * y + '1' * r)
    else:
         print('1' * l + '0' * (y - diff) + '1' + '0' * diff + '1' * r)