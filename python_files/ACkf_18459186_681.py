import sys
if __name__ == "__main__":
    #n, m = list(map(int, input().split()))
    n = int(input())
    p = [list(input().split()) for _ in range(n)]
    for i in range(n):
        if int(p[i][1]) >= 2400 and int(p[i][2]) > int(p[i][1]):
            print("YES")
            sys.exit(0)
    print("NO")