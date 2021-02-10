from queue import PriorityQueue

fmap = lambda f,l: list(map(f,l))
parse_int = lambda: fmap(int, input().split())

prl, prr = 0, 0
il, ir = 0,0
lsum, rsum = 0,0

for idx in range(int(input())):
    l, r = parse_int()
    lsum += l
    rsum += r

    if r-l > prl:
        il = idx
        prl = r-l
    if l-r > prr:
        ir = idx
        prr = l-r

if lsum+prl > rsum+prr:
    if prl>0:
        print(il+1)
    else:
        print(0)
else:  # right > left
    if prr>0:
        print(ir+1)
    else:
        print(0)