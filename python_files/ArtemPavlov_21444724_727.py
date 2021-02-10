a, b = map(int, input().split())


def nxt(seq):
    global b
    x = seq[-1]
    if not x > b:
        if x == b:
            return seq
        seq2 = seq.copy()
        seq2.append(int(str(seq[-1]) + "1"))
        ret = nxt(seq2)
        if ret:
            return ret
        seq2 = seq.copy()
        seq2.append(seq[-1] * 2)
        ret = nxt(seq2)
        if ret:
            return ret
    else:
        return False


ans = nxt([a])
if ans:
    print("YES")
    print(len(ans))
    print(*ans)
else:
    print("NO")