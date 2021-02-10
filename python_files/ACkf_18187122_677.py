if __name__ == "__main__":
    #n, m = list(map(int, input().split()))
    n, h = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if A[i] > h:
            cnt += 1
    print(n + cnt)