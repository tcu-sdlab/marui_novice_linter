import sys
x = sorted(list(map(int, sys.stdin.readline().split(" "))))


print(x[1] - x[0] + x[2] - x[1])