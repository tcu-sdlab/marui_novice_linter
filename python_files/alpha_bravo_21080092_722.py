n = int(input())
p = list(map(int, input().split()))
c = "aeiouy"


def main():
    for i in range(n):
        s = input()
        count = 0

        for ch in s:
            if ch in c:
                count += 1

        if count != p[i]:
            print("NO")
            return

    print("YES")
    return

main()