from collections import defaultdict
import sys, os, math

if __name__ == "__main__":
    #n, m = list(map(int, input().split()))
    #sys.stdout.flush()
    l1, r1, l2, r2, k = map(int, input().split())
    if l1 > r2 or l2 > r1:
        print(0)
        sys.exit(0)
    l, r = max(l1, l2), min(r1, r2)
    if k >= l and k <= r:
        print(r - l)
    else:
        print(r - l + 1)