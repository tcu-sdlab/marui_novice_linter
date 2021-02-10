from collections import defaultdict
import sys, os, math

if __name__ == "__main__":
    #n, m = list(map(int, input().split()))
    #sys.stdout.flush()
    n = int(input())
    p = list(map(int, input().split()))
    for i in range(n):
        s = input()
        cnt = 0
        for ch in "aeiouy":
            cnt += s.count(ch)
        if cnt != p[i]:
            print("NO")
            sys.exit(0)
    print("YES")