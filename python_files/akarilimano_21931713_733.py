# coding=utf-8
__author__ = 'Alexander'

n = input()

n = int(n)

l = []
r = []
L0 = 0
R0 = 0

for i in range(n):
    s = input()
    lt, rt = map(int, s.split())
    l.append(lt)
    r.append(rt)
    L0 += lt
    R0 += rt

B0 = abs(L0-R0)
# print(L0, R0, B0)

BN = B0
N = 0

for i in range(n):
    L = L0 - l[i] + r[i]
    R = R0 - r[i] + l[i]
    B = abs(L-R)

    if B > BN:
        BN = B
        N = i+1

    # print(L, R, B)

print(N)