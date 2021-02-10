from collections import defaultdict
import sys, os, math

if __name__ == "__main__":
    #n, m = list(map(int, input().split()))
    n = int(input())
    s = [list(map(int, input().split())) for i in range(n)]
    if n == 1:
        print(1)
        sys.exit(0)
    pos = []
    for i in range(n):
        for j in range(n):
            if s[i][j] == 0:
                pos = [i, j]
                break;
    val = sum(s[(pos[0] + 1) % n])
    s[pos[0]][pos[1]] = max(val - sum(s[pos[0]]), 1)
    #check
    for i in range(n):
        if sum(s[i]) != val:
            print(-1)
            sys.exit(0)
    for j in range(n):
        t = 0
        for i in range(n):
            t += s[i][j]
        if t != val:
            print(-1)
            sys.exit(0)
    t, tt = 0, 0
    for i in range(n):
        t += s[i][i]
        tt += s[i][n - 1 - i]
    if t != val or tt != val:
        print(-1)
        sys.exit(0)
           
    print(s[pos[0]][pos[1]])
    '''
    for i in range(n):
        print(' '.join(map(str, s[i])))
    '''