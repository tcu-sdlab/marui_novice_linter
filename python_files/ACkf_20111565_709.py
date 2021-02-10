from collections import defaultdict
import sys, os, math

if __name__ == "__main__":
    #n, m = list(map(int, input().split()))
    n, b, d = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt, sm = 0, 0
    for i in arr:
        if i > b:
            continue
        sm += i
        if sm > d:
            sm = 0
            cnt += 1
    print(cnt)