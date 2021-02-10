a, b = map(float, input().split())
d = 1000000000000
for i in range(int(input())):
    x, y, v = map(float, input().split())
    A, B = abs(y - b), abs(x - a)
    C = (A * A + B * B) ** 0.5
    d = min(d, C / v)
print(d)