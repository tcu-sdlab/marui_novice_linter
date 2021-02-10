a, b = map(int, input().split())

def main(a, b, ans, n):
    global out
    if a == b:
        out =  [
    str(a) + ' ' + ans, n + 1]
        return
    b_s = str(b)
    if b > a and b_s[-1] == '1':
        main(a, int(b_s[:-1]), b_s + ' ' + ans, n + 1)
        return
    if b > a and b % 2 == 0:
        main(a, b // 2, b_s + ' ' + ans, n + 1)
        return
    else:
        out = ['youcannot', n]
        return

main(a, b, '', 0)

if out[0] == 'youcannot':
    print('NO')
else:
    print('YES')
    print(out[1])
    print(out[0])