from collections import defaultdict
import sys, os, math

if __name__ == "__main__":
    #n, m = list(map(int, input().split()))
    #sys.stdout.flush()
    n, k = map(int, input().split())
    cnt = [0] * 110
    for i in range(n):
        s = input()
        cnt[len(s)] += 1
    s = input()
    t = sum(cnt[:len(s)])
    print(t + t // k * 5 + 1, t + cnt[len(s)] + (t + cnt[len(s)] - 1) // k * 5)