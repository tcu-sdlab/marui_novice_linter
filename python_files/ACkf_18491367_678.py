from collections import defaultdict
import sys

def mpow(base, p):
    temp = 1
    while p:
        if (p & 1):
            temp = (temp * base) % MOD
        p //= 2
        base = (base * base) % MOD
    return temp % MOD
if __name__ == "__main__":
    #n, m = list(map(int, input().split()))
    a, b, n, x = map(int, input().split())
    MOD = 10 ** 9 + 7
    temp = mpow(a, n)
    if a > 1:
        ans = ((temp * x % MOD) + (b * (temp - 1) % MOD) * mpow(a - 1, MOD - 2) % MOD) % MOD
    else:
        ans = ((temp * x % MOD) + b * (n % MOD) % MOD) % MOD
    print(ans)