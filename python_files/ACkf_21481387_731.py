from collections import defaultdict
import sys, os, math

if __name__ == "__main__":
    #n, m = list(map(int, input().split()))
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n):
        if arr[i] % 2 != 0:
            if i == n - 1 or arr[i + 1] == 0:
                print("NO")
                sys.exit(0)
            arr[i + 1] -= 1
    print("YES")