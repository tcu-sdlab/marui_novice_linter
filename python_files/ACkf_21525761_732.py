from collections import defaultdict
import sys, os, math

if __name__ == "__main__":
    #n, m = list(map(int, input().split()))
    k, r = map(int, input().split())
    for i in range(1, 11):
        if i * k % 10 == r or i * k % 10 == 0:
            print(i)
            sys.exit(0)