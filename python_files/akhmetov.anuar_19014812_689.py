from queue import Queue

n = int(input())
a = input().split(' ')
used = []
d = []
for i in range(0, n):
    used.append(False)
    d.append(-1)
q = Queue()
q.put(0)
d[0] = 0
while not (q.empty()):
    v = q.get()
    for dl in range(-1, +2):
        u = v + dl
        if 0 <= u and u < n and d[u] == -1:
            d[u] = d[v] + 1
            q.put(u)
    u = int(a[v]) - 1
    if d[u] == -1:
        d[u] = d[v] + 1
        q.put(u)
for i in range(0, n):
    print(d[i])