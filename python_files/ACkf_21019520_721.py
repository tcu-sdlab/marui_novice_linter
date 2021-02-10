from collections import defaultdict
import sys, os, math

if __name__ == "__main__":
    #n, m = list(map(int, input().split()))
    #sys.stdout.flush()
    n = int(input())
    s = input()
    ans = []
    cnt = 0
    for i in range(len(s)):
        if s[i] == 'B':
            cnt += 1
            if i == len(s) - 1:
                ans.append(cnt)
        else:
            if cnt > 0:
                ans.append(cnt)
                cnt = 0
    print(len(ans))
    print(' '.join(str(num) for num in ans))