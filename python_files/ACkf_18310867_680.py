from collections import defaultdict

if __name__ == "__main__":
    #n, m = list(map(int, input().split()))
    n, a = map(int, input().split())
    A = list(map(int, input().split()))
    ans, i = sum(A), 1
    while a - 1 - i >= 0 and a - 1 + i <= n - 1:
        if A[a - 1 - i] != A[a - 1 + i]:
            ans -= 1
        i += 1
    print(ans)