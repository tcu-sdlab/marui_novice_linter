from collections import defaultdict
import sys

def gcd(x, y):
    if y == 0: return x
    return gcd(y, x % y)
if __name__ == "__main__":
    #n, m = list(map(int, input().split()))
    n, a, b, p, q = map(int, input().split())
    
    if p > q:
        print(n // a * p + (n // b - n // (a * b // gcd(a, b))) * q)
    else:
        print(n // b * q + (n // a - n // (a * b // gcd(a, b))) * p)