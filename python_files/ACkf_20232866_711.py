from collections import defaultdict
import sys, os, math

if __name__ == "__main__":
    #n, m = list(map(int, input().split()))
    n = int(input())
    s = list(input() for i in range(n))
    for i in range(n):
        if s[i][:2] == "OO":
           s[i] = "++" + s[i][2:]
           break
        elif s[i][3:] == "OO":
            s[i] = s[i][:3] + "++" 
            break
        if i == n - 1:
            print("NO")
            sys.exit(0)
    print("YES")
    for i in range(n):
        print(s[i])