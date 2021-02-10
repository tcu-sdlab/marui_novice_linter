from collections import defaultdict
import sys

if __name__ == "__main__":
    #n, m = list(map(int, input().split()))
    y = int(input())
    cnt = 0
    leap = lambda y : y % 400 == 0 or (y % 100 != 0 and y % 4 == 0)
    f = leap(y)
    while True:
        y += 1
        if leap(y):
            cnt += 2
        else:
            cnt += 1
        if leap(y + 1) == f:
            if f and cnt % 7 == 5 or (not f and cnt % 7 == 6):
                break
    print(y + 1)