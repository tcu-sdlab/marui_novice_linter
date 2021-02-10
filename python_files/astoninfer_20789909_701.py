def idx(x):
    if x > 'Z':
        return ord(x) - ord('a') + 26
    else:
        return ord(x) - ord('A')


def check():
    tmp = 0
    for i in range(52):
        if buf[i]:
            tmp |= 1 << i
    return (tmp & syb) == syb


n = int(input())
s = input()
syb = 0
c = [[] for i in range(n + 1)]
for i in range(1, n + 1):
    c[i] = [0] * 52
    c[i][idx(s[i - 1])] += 1
    syb |= 1 << idx(s[i - 1])
ans = 0x3f3f3f3f
l = 1
r = 1
buf = c[1]
while r <= n:
    if check():
        while buf[idx(s[l - 1])] > 1:
            buf[idx(s[l - 1])] -= 1
            l += 1
        ans = min(ans, r - l + 1)
    r += 1
    if r <= n:
        buf[idx(s[r - 1])] += 1
print(ans)