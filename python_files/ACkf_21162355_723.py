from collections import defaultdict
import sys, os, math

if __name__ == "__main__":
    #n, m = list(map(int, input().split()))
    #sys.stdout.flush()
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = [0] * 2100
    t, d = n // m, n % m
    chan = 0
    for i in range(n):
        if arr[i] <= m:
            cnt[arr[i]] += 1
    for i in range(n):
        if arr[i] <= m:
            if cnt[arr[i]] <= t:
                pass
            elif d > 0:
                d -= 1
                #cnt[arr[i]] -= 1
            else:
                for j in range(1, m + 1):
                    if cnt[j] < t:
                        cnt[j] += 1
                        cnt[arr[i]] -= 1
                        arr[i] = j
                        chan += 1
                        break
        else:
            for j in range(1, m + 1):
                if cnt[j] < t:
                    cnt[j] += 1
                    arr[i] = j
                    chan += 1
                    f = False
                    break
            continue;
            '''
            if f:
                for j in range(1, m + 1):
                    if cnt[j] >= t and cnt[j] < t + d and d > 0:
                        cnt[j] += 1
                        d -= 1
                        arr[i] = j
                        chan += 1
                        break
            '''
    print(t, chan)
    print(' '.join(str(s) for s in arr))
    #print(cnt[1:m + 1])