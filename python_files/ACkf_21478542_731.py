from collections import defaultdict
import sys, os, math

if __name__ == "__main__":
    #n, m = list(map(int, input().split()))
    s = input()
    pos, ans = 0, 0
    for i in range(len(s)):
        if i == 0:
            ans += min(abs(ord(s[i]) - ord('a')), 26 - abs(ord(s[i]) - ord('a')))
        else:
            ans += min(abs(ord(s[i]) - ord(s[i - 1])), 26 - abs(ord(s[i]) - ord(s[i - 1])))
    print(ans)