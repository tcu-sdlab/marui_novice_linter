from collections import defaultdict
import sys

if __name__ == "__main__":
    #n, m = list(map(int, input().split()))
    A = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 4, 9, 25, 49]
    #59, 61, 67, 71, 73, 79, 83, 89, 97]
    cnt = 0
    for i in range(20):
        print(A[i])
        sys.stdout.flush()
        s = input()
        if s == "yes":
            cnt += 1
    if cnt <= 1:
        print("prime")
    else:
        print("composite")