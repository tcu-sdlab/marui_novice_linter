from collections import defaultdict

if __name__ == "__main__":
    #n, m = list(map(int, input().split()))
    A = list(map(int, input().split()))
    A.sort()
    ans = sum(A)
    if A[4] == A[3]:
        ans = min(ans, sum(A[:3]))
        if A[3] == A[2]:
            ans = min(ans, sum(A[:2]))
    if A[3] == A[2]:
        ans = min(ans, A[0] + A[1] + A[4])
        if A[2] == A[1]:
            ans = min(ans, A[0] + A[4])
    if A[2] == A[1]:
        ans = min(ans, A[0] + A[3] + A[4])
        if A[1] == A[0]:
            ans = min(ans, A[3] + A[4])
    if A[1] == A[0]:
        ans = min(ans, sum(A[2:]))
    print(ans)