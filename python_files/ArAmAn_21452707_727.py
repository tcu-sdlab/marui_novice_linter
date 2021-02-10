def delenie(n):
    if n % 2 == 0:
        return n // 2
    else:
        return -1


def delenie2(n):
    if (n - 1) % 10 == 0:
        return (n - 1) // 10
    else:
        return -1


def main(a1, b1, ans):
    if b1 == a1:
        print('YES')
        return ans
    elif b1 < a1:
        print('NO')
        exit()
    else:
        c = delenie(b1)
        c1 = delenie2(b1)
        if c != -1:
            ans.append(c)
            main(a1, c, ans)
        if c1 != -1:
            ans.append(c1)
            main(a1, c1, ans)
        if c == -1 and c1 == -1:
            print('NO')
            exit()


a, b = map(int, input().split())
ans = []
main(a, b, ans)
ans.reverse()
ans.append(b)
print(len(ans))
print(*ans)