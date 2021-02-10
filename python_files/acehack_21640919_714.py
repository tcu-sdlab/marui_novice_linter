# Tags: #bits, #bitmask

t = int(input())
dc = [0]*(2**19)
tt = str.maketrans('0123456789', '0101010101')

for i in range(0, t):
    st = input().split()
    if st[0] == '+':
        dc[int(st[1].translate(tt), 2)] += 1
    elif st[0] == '-':
        dc[int(st[1].translate(tt), 2)] -= 1
    else:
        mu = int(st[1], 2)
        print(dc[mu])