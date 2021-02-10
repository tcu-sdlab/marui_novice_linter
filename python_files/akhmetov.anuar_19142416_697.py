n = int(input())
t1 = {}
t2 = {}
for i in range(n):
    q = list(map(int, input().split()))
    if q[0] == 1:
        _, u, v, w = q
        while (u != v):
            v, u = max(u, v), min(u, v)
            if v & 1 == 1:
                t2[v] = t2.get(v, 0) + w
                v = (v - 1) // 2
            else:
                t1[v] = t1.get(v, 0) + w
                v = v // 2
    else:
        _, u, v = q
        c = 0
        while (u != v):
            v, u = max(u, v), min(u, v)
            if v & 1 == 1:
                c += t2.get(v, 0)
                v = (v - 1) // 2
            else:
                c += (t1.get(v, 0))
                v = v // 2
        print(c)