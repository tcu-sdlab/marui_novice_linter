import sys, string
#sys.stdin = open("apples.in","r")
#sys.stdout = open("apples.out","w")


sys.setrecursionlimit(2000000000)
flag = False
n, m = list(map(int, sys.stdin.readline().split()))
lst = [['' for i in range(2 * m + 2)] for j in range(n)]
for i in range(n):
    lst[i] = [x for x in input().split()]
    for j in range(m):
        if (lst[i][j] in {'C', 'M', 'Y'}):
            flag = True

if (flag):
    print("#Color")
else:
    print("#Black&White")