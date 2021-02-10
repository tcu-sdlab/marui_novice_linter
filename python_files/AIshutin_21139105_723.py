x, y, z = map(int, input().split())
q = abs(x - y) + abs(x - z)
w = abs(y - z) + abs(y - x)
e = abs(z - x) + abs(z -y)
s = (x + y + z) / 3
d = int(abs(x - s) + abs(y - s) + abs(z - s))
print(min(q, w, e))