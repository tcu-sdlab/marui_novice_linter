from collections import defaultdict
import sys, os, math

if __name__ == "__main__":
    #n, m = list(map(int, input().split()))
    s = input()
    ss = "abcdefghijklmnopqrstuvwxyz"
    sss = ''
    if s[0] != 'a':
        for i in range(len(s)):
            if s[i] == 'a':
                sss += s[i:]
                break
            sss += ss[ord(s[i]) - ord('a') - 1]
    else:
        pos = 0
        while pos < len(s) and s[pos] == 'a':
            pos += 1
        if pos == len(s):
            for i in range(len(s) - 1):
                sss += 'a'
            print(sss + 'z')
            sys.exit(0)
        sss += s[:pos]
        for i in range(pos, len(s)):
            if s[i] == 'a':
                sss += s[i:]
                break
            sss += ss[ord(s[i]) - ord('a') - 1]
    print(sss)