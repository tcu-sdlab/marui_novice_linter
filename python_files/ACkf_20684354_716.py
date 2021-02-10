from collections import defaultdict
import sys, os, math

if __name__ == "__main__":
    #n, m = list(map(int, input().split()))
    #sys.stdout.flush()
    n, c = map(int, input().split())
    time = list(map(int, input().split()))
    ans = 1
    for i in range(1, n):
        if time[i] - time[i - 1] <= c:
            ans += 1
        else:
            ans = 1
    print(ans)