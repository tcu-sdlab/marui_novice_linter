from collections import defaultdict
import sys, os, math

if __name__ == "__main__":
    #n, m = list(map(int, input().split()))
    week = [ "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    s1 = input()
    s2 = input()
    if (week.index(s2) - week.index(s1) + 7) % 7 in [0, 2, 3]:
        print("YES")
    else:
        print("NO")