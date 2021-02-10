from collections import defaultdict
import sys

if __name__ == "__main__":
    #n, m = list(map(int, input().split()))
    n = int(input())
    index = list(map(int, input().split()))
    index.sort()
    print(index[(n - 1) // 2])