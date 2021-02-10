if __name__ == "__main__":
    #n, m = list(map(int, input().split()))
    n = int(input())
    a = list(map(int, input().split()))
    l, r = 0, 0
    for i in range(n):
        if a[i] == 1:
            l = i
        elif a[i] == n:
            r = i
    print(max(abs(r - 0), abs(r - n + 1), abs(0 - l), abs(n - l - 1)))