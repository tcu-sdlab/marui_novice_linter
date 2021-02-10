n, c = [int(i) for i in input().split()]
t = [int(i) for i in input().split()]

w = []
for i in range(len(t)):
    if len(w) > 0:
        if t[i] - t[i - 1] > c:
            w = []
    w.append(t[i])

print(len(w))