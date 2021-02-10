from collections import defaultdict
import sys

if __name__ == "__main__":
    #n, m = list(map(int, input().split()))
    n, k = map(int, input().split())
    print(n // k * k + k)