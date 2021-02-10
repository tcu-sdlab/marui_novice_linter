from collections import defaultdict
import sys

if __name__ == "__main__":
    #n, m = list(map(int, input().split()))
    p = input()
    if p in ["a8", "a1", "h8", "h1"]:
        print(3)
    elif p[0] in "ah" or p[1] in "18":
        print(5)
    else:
        print(8)