from sys import setrecursionlimit
setrecursionlimit(1000000000)

def main():
    a, b, c=[int(i) for i in input().split()]
    if ((a//2==b) and (a//2==c)) or ((a//2==b-1) and (a//2==c)) or ((a//2==b) and (a//2==c-1)) or ((a//2==b-1) and (a//2==c-1)):
        print("NO")
        return 0
    print("YES")


main()