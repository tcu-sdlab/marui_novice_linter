from collections import defaultdict
import sys, os, math

if __name__ == "__main__":
    #n, m = list(map(int, input().split()))
    #sys.stdout.flush()
    x = list(map(int, input().split()))
    ans = 300
    for i in range(min(x), max(x) + 1):
        tmp = abs(i - x[0]) + abs(i - x[1]) + abs(i - x[2])
        if tmp < ans:
            ans = tmp
    print(ans)