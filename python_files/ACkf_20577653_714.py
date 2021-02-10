from collections import defaultdict
import sys, os, math

if __name__ == "__main__":
    #n, m = list(map(int, input().split()))
    #sys.stdout.flush()
    n = int(input())
    arr = list(map(int, input().split()))
    temp = []
    for num in arr:
        if num not in temp:
            temp.append(num)
        if len(temp) > 3:
            print("NO")
            sys.exit(0)
    temp.sort()
    if len(temp) < 3 or temp[0] + temp[2] == 2 * temp[1]:
        print("YES")
    else:
        print("NO")