from collections import defaultdict
import sys

if __name__ == "__main__":
    #n, m = list(map(int, input().split()))
    n = int(input())
    table = [[0] * 100 for _ in range(100)]
    i, j = 0, n // 2
    for num in range(1, n * n + 1):
        table[i][j] = num
        if table[(i - 1 + n) % n][(j + 1 + n) % n] == 0:
            i = (i - 1 + n) % n
            j = (j + 1 + n) % n
        else:
            i = (i + 1 + n) % n       
    for i in range(n):
        print(' '.join([str(j) for j in table[i][:n]]))