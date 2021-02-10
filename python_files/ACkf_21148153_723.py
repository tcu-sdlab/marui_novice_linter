from collections import defaultdict
import sys, os, math

if __name__ == "__main__":
    #n, m = list(map(int, input().split()))
    #sys.stdout.flush()
    n = int(input())
    s = input()
    par = False
    lon, cnt = 0, 0 
    s1, s2 = "", ""
    for i in range(n):
        if s[i] == '(':
            par = True
            s1 += '_'
            s2 += '_'
        elif s[i] == ')':
            par = False
            s1 += '_'
            s2 += '_'
        else:
            if par:
                s1 += s[i]
            else:
                s2 += s[i]
    lon = max([len(ss) for ss in s2.split('_')])
    #print(s1, s2)
    for ss in s1.split('_'):
        if ss != "":
            cnt += 1
    print(lon, cnt)