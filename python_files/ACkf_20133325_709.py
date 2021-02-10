from collections import defaultdict
import sys, os, math

def solve(arr, a):
    if a <= arr[0]:
        return arr[n - 2] - a
    elif a >= arr[n - 2]:
        return a - arr[0]
    return min(2 * (arr[n - 2] - arr[0]) - abs(a - arr[0]), 2 * (arr[n - 2] - arr[0]) - abs(arr[n - 2] - a))
if __name__ == "__main__":
    #n, m = list(map(int, input().split()))
    n, aa = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if n == 1:
        print(0)
    else:
        print(min(solve(A[:n - 1], aa), solve(A[1:], aa)))